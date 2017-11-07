package org.openex.tcpc;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.j256.ormlite.dao.Dao;
import com.j256.ormlite.dao.DaoManager;
import com.j256.ormlite.jdbc.JdbcConnectionSource;
import org.apache.commons.lang3.StringEscapeUtils;
import org.apache.commons.lang3.time.DateUtils;
import org.apache.log4j.PropertyConfigurator;
import org.openex.tcpc.bean.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.io.FileWriter;
import java.sql.SQLException;
import java.text.ParseException;
import java.util.Collections;
import java.util.Date;
import java.util.List;

/**
 * Created by huash06 on 2015/6/27.
 */
public class Sqlite2Json {
    private static final String DATABASE_URL = "jdbc:sqlite:tc.sqlite";
    private static final Logger logger = LoggerFactory.getLogger(Sqlite2Json.class);

    public static void main(String[] args) {

        PropertyConfigurator.configure("log4j.properties");
        new File("result").mkdirs();
        // sqlite2SingleJson();
        sqlite2DistributeJson();
    }

    private static void sqlite2DistributeJson() {
        JdbcConnectionSource connectionSource = null;
        try {
            connectionSource = new JdbcConnectionSource(DATABASE_URL);
            Dao<TCMatch, Integer> matchDao = DaoManager.createDao(connectionSource, TCMatch.class);
            Dao<TCProblem, Integer> problemDao = DaoManager.createDao(connectionSource, TCProblem.class);

            TCMatchArchive archive = new TCMatchArchive();
            List<TCMatch> matches = matchDao.queryForAll();

            matches.stream().forEach(
                    match -> {
                        try {
                            List<TCProblem> problems = problemDao.queryForEq("match_id", match.getId());

                            problems.parallelStream()
                                    .forEach(problem -> {
                                        problem.setMatch(null);
                                        jsonfyObject(problem, "problem/" + problem.getId());
                                    });

                            logger.info("Found match {}", match);

                            problems.parallelStream().forEach(problem -> {
                                problem.setStatement(StringEscapeUtils.unescapeHtml4(problem.getStatement().substring(
                                        0, Math.min(100, problem.getStatement().length()))));
                                problem.setDefinition(null);
                                problem.setConstraints(null);
                                problem.setExamples(null);
                                problem.setNotes(null);
                            });
                            match.setProblems(problems);
                        } catch (Exception e) {
                            logger.error(e.getLocalizedMessage(), e);
                        }
                    });

            logger.info("Sorting matches...");

            Collections.sort(matches, (m1, m2) -> {
                Date d1 = null;
                Date d2 = null;
                try {
                    d1 = DateUtils.parseDate(m1.getTime(), "MM.dd.yyyy");
                    d2 = DateUtils.parseDate(m2.getTime(), "MM.dd.yyyy");
                    return d2.compareTo(d1);
                } catch (ParseException e) {
                    e.printStackTrace();
                    if (d1 == null) {
                        return 1;
                    } else {
                        return -1;
                    }
                }
            });

            archive.setMatches(matches);
            jsonfyObject(archive, "archive");


        } catch (Exception e) {
            logger.error(e.getLocalizedMessage(), e);
        } finally {
            if (connectionSource != null) {
                try {
                    connectionSource.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public static void sqlite2SingleJson() {
        JdbcConnectionSource connectionSource = null;
        try {
            connectionSource = new JdbcConnectionSource(DATABASE_URL);
            Dao<TCMatch, Integer> matchDao = DaoManager.createDao(connectionSource, TCMatch.class);
            Dao<TCProblem, Integer> problemDao = DaoManager.createDao(connectionSource, TCProblem.class);
            Dao<TCProblemClassDefinition, Integer> defDao = DaoManager.createDao(connectionSource,
                    TCProblemClassDefinition.class);
            Dao<TCProblemExample, Integer> expDao = DaoManager.createDao(connectionSource, TCProblemExample.class);
            Dao<TCProblemNote, Integer> noteDao = DaoManager.createDao(connectionSource, TCProblemNote.class);
            Dao<TCProblemConstraint, Integer> constDao = DaoManager.createDao(connectionSource,
                    TCProblemConstraint.class);

            TCMatchArchive archive = new TCMatchArchive();
            List<TCMatch> matches = matchDao.queryForAll();
            for (TCMatch match : matches) {
                List<TCProblem> problems = problemDao.queryForEq("match_id", match.getId());
                match.setProblems(problems);
                logger.info("Found match {}", match);
            }
            archive.setMatches(matches);

            jsonfyObject(archive, "archive_pretry");

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            if (connectionSource != null) {
                try {
                    connectionSource.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    private static void jsonfyObject(Object object, String fileName) {
        logger.info("JSONFING... " + object.toString());
        try {
            File f = new File("result/" + fileName + ".json");
            if (!f.getParentFile().exists() && !f.getParentFile().mkdirs()) {
                logger.error("Failed to created dir " + f.getParent());
                return;
            }
            FileWriter writer = new FileWriter(f);
            Gson gson = new GsonBuilder().disableHtmlEscaping().setPrettyPrinting().create();
            gson.toJson(object, writer);
            writer.close();
        } catch (Exception e) {
            logger.warn("Error while jsonfy " + object.toString(), e);
        }
    }
}
