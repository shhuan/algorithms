package org.openex.tcpc;

import com.alibaba.fastjson.JSON;
import com.j256.ormlite.dao.Dao;
import com.j256.ormlite.dao.DaoManager;
import com.j256.ormlite.jdbc.JdbcConnectionSource;
import com.j256.ormlite.table.TableUtils;
import org.apache.commons.codec.digest.DigestUtils;
import org.apache.commons.lang3.StringUtils;
import org.apache.log4j.PropertyConfigurator;
import org.openex.tcpc.bean.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Match2Sqlite {

    // static String DATABASE_URL = "jdbc:h2:mem:match";
    // "jdbc:sqlite::memory:"
    final static String DATABASE_URL = "jdbc:sqlite:tc.sqlite";
    private static final Logger logger = LoggerFactory.getLogger(Match2Sqlite.class);

    public static void main(String[] args) {
        PropertyConfigurator.configure("log4j.properties");
        logger.info("Starting...");
        createTables();

        try {
            List<TCMatch> matchBasicInfos = new ArrayList<>();
            Files.find(Paths.get("data"), 1, (path, attr) -> String.valueOf(path).endsWith("json"))
                    .map(f -> JSON.parseObject(readFile(f), TCMatchArchive.class).getMatches())
                    .forEach(matchBasicInfos::addAll);

            Files.find(Paths.get("data/matches"), 1, ((path, basicFileAttributes) -> String.valueOf(path).endsWith("json")))
                    .parallel()
                    .forEach(
                            mf -> {
                                TCMatch match = JSON.parseObject(readFile(mf), TCMatch.class);
                                match.copyBasicInfo(matchBasicInfos.stream().filter(s -> s.hasSameLink(match))
                                        .findFirst().get());

                                String matchMd5 = DigestUtils.md5Hex(match.getLink());
                                try {
                                    match.setProblems(Files
                                            .list(new File("data/problems/" + matchMd5).toPath())
                                            .parallel()
                                            .filter(pf -> pf.getFileName().toString().endsWith("json"))
                                            .map(pf -> {
                                                TCProblem problem = null;
                                                try {
                                                    problem = JSON.parseObject(readFile(pf), TCProblem.class);
                                                } catch (Exception e) {
                                                    logger.error(e.getLocalizedMessage(), e);
                                                }

                                                if (problem != null && StringUtils.isNotBlank(problem.getLink())) {
                                                    final TCProblem problemRef = problem;
                                                    problem.copyBasicInfo(match.getProblems().stream().filter(p -> p.hasSameLink(problemRef)).findFirst().orElse(problem));
                                                } else {
                                                    logger.error("json file of problem is invalid: " + pf.toString());
                                                    match.getProblems().stream().map(p -> DigestUtils.md5Hex(p.getLink())).forEach(System.out::println);
                                                    problem = match.getProblems().stream().filter(
                                                            p -> String.format("%s.json", DigestUtils.md5Hex(p.getLink())).equals(pf.getFileName().toString())
                                                    ).findFirst().orElse(problem);
                                                }
                                                return problem;
                                            }).filter(p -> p != null).map(p -> {
                                                if (StringUtils.isBlank(p.getStatement())) {
                                                    p.setStatement("Unknown statement");
                                                }
                                                return p;
                                            }).collect(Collectors.toList()));
                                } catch (IOException e) {
                                    logger.error(e.getLocalizedMessage(), e);
                                }
                                persistMatch(match);
                            });
        } catch (IOException e) {
            logger.error(e.getLocalizedMessage(), e);
        }

    }

    private static String readFile(Path path) {
        logger.info("reading " + path.toString());
        try {
            return Files.lines(path).collect(Collectors.joining());
        } catch (IOException e) {
            logger.error(e.getLocalizedMessage(), e);
        }
        return "";
    }

    public static void createTables() {
        JdbcConnectionSource connectionSource = null;
        try {
            connectionSource = new JdbcConnectionSource(DATABASE_URL);
            TableUtils.createTableIfNotExists(connectionSource, TCMatch.class);
            TableUtils.createTableIfNotExists(connectionSource, TCProblem.class);
            TableUtils.createTableIfNotExists(connectionSource, TCProblemClassDefinition.class);
            TableUtils.createTableIfNotExists(connectionSource, TCProblemExample.class);
            TableUtils.createTableIfNotExists(connectionSource, TCProblemNote.class);
            TableUtils.createTableIfNotExists(connectionSource, TCProblemConstraint.class);

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            if (connectionSource != null) {
                try {
                    connectionSource.close();
                } catch (SQLException e) {
                    logger.error(e.getLocalizedMessage(), e);
                }
            }
        }
    }

    public static void persistMatch(final TCMatch match) {

        logger.info("Persisting Match in " + Thread.currentThread().getName());

        logger.info(match.toString());
        logger.info("=================Persisting Match==================");

        JdbcConnectionSource connectionSource = null;
        try {
            connectionSource = new JdbcConnectionSource(DATABASE_URL);
            Dao<TCMatch, Integer> matchDao = DaoManager.createDao(connectionSource, TCMatch.class);
            Dao<TCProblem, Integer> problemDao = DaoManager.createDao(connectionSource, TCProblem.class);

            matchDao.create(match);
            match.getProblems().stream().forEach(problem -> {
                problem.setMatch(match);
                try {
                    problemDao.create(problem);
                } catch (Exception e) {
                    logger.error(e.getLocalizedMessage(), e);
                }
            });

            logger.info("=================Inserted Problems==================");
            for (TCProblem p : problemDao.queryForAll()) {
                logger.info(p.toString());
            }
            logger.info("=================Inserted Problems==================");
        } catch (SQLException e) {
            logger.error(e.getLocalizedMessage(), e);
        } finally {
            if (connectionSource != null) {
                try {
                    connectionSource.close();
                } catch (SQLException e) {
                    logger.error(e.getLocalizedMessage(), e);
                }
            }
        }

    }
}
