/**
 * 
 */
package org.openex.tcpc;

import org.apache.commons.codec.digest.DigestUtils;
import org.apache.commons.lang3.StringEscapeUtils;
import org.junit.*;
import org.openex.tcpc.bean.*;

import java.util.ArrayList;
import java.util.List;


/**
 * @author huash06
 *
 */
public class JSonComposerTest {

	/**
	 * @throws java.lang.Exception
	 */
	@Before
	public void setUp() throws Exception {	
		Match2Sqlite.createTables();
	}

	/**
	 * @throws java.lang.Exception
	 */
	@After
	public void tearDown() throws Exception {
	}

	@Test
	@Ignore
	public void testStringReplace(){
		String statement = "<td class=\"statText\">In this problem we are dealing with a string of N bits, numbered from 0 to N-1.<br /><br /> Julia likes the string that consists of N zeros.<br /><br /> If you give her any N-bit string, she will convert it into a string of N zeros using the smallest possible number of actions.<br /><br /> An action consists of selecting an integer k (1 &lt;= k &lt;= N) and flipping either the first k bits or the last k bits of the string.<br /><br /> Formally, Julia can flip either all bits with number i such that i &lt; k or all bits with number i such that i &gt;= N - k.<br /><br /> <br /><br /> You are going to generate a random string of N bits.<br /><br /> You are given a int[] <b>p</b> with N elements.<br /><br /> For each i, bit number i has a <b>p</b>[i] percent chance of being a 1 and a (100 - <b>p</b>[i]) percent chance of being a 0.<br /><br /> The values of the bits are chosen independently from each other.<br /><br /> <br /><br /> After you generate the string, you are going to give it to Julia.<br /><br /> Please find and return the expected number of actions Julia will take.</td>";
		statement = statement.replaceFirst("^<td[^>]*>", "");
		statement = statement.replaceFirst("</td>$", "");
		Assert.assertEquals("In this problem we are dealing with a string of N bits, numbered from 0 to N-1.<br /><br /> Julia likes the string that consists of N zeros.<br /><br /> If you give her any N-bit string, she will convert it into a string of N zeros using the smallest possible number of actions.<br /><br /> An action consists of selecting an integer k (1 &lt;= k &lt;= N) and flipping either the first k bits or the last k bits of the string.<br /><br /> Formally, Julia can flip either all bits with number i such that i &lt; k or all bits with number i such that i &gt;= N - k.<br /><br /> <br /><br /> You are going to generate a random string of N bits.<br /><br /> You are given a int[] <b>p</b> with N elements.<br /><br /> For each i, bit number i has a <b>p</b>[i] percent chance of being a 1 and a (100 - <b>p</b>[i]) percent chance of being a 0.<br /><br /> The values of the bits are chosen independently from each other.<br /><br /> <br /><br /> After you generate the string, you are going to give it to Julia.<br /><br /> Please find and return the expected number of actions Julia will take.", statement);
	}

	@Test
	public void testStringEscape(){
		System.out.println(StringEscapeUtils.escapeHtml3("&nbsp;"));
		System.out.println(StringEscapeUtils.escapeJava("&nbsp;"));
		System.out.println(StringEscapeUtils.escapeHtml4("&nbsp;"));
		System.out.println(StringEscapeUtils.unescapeHtml3("&nbsp;"));
		System.out.println(StringEscapeUtils.unescapeHtml4("&nbsp;"));
		System.out.println(StringEscapeUtils.unescapeJava("&nbsp;"));
		System.out.println("============================");
		System.out.println(StringEscapeUtils.escapeHtml4(" "));
		System.out.println(StringEscapeUtils.escapeHtml3(" "));
		System.out.println(StringEscapeUtils.escapeJava(" "));
		System.out.println(StringEscapeUtils.escapeHtml4(">"));
		System.out.println(StringEscapeUtils.unescapeHtml4("&gt;"));
		System.out.println(StringEscapeUtils.unescapeHtml3("&gt;"));
		System.out.println(StringEscapeUtils.unescapeJava("&gt;"));
//		Assert.assertTrue(StringUtils.isBlank(StringEscapeUtils.unescapeJava("&nbsp;")));
		System.out.println("============================");
		System.out.println(StringEscapeUtils.unescapeHtml4("compare a and b: a&gt;b"));

	}

    @Test
    public void testDigest(){
        String md5 = DigestUtils.md5Hex("http://community.topcoder.com/stat?c=problem_statement&pm=11295&rd=14537");
        for(int i=0; i<100; i++){
            Assert.assertEquals(md5, DigestUtils.md5Hex("http://community.topcoder.com/stat?c=problem_statement&pm=11295&rd=14537"));
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }

	@Ignore
	@Test
	public void testPersistMatch() {
		TCMatch match = new TCMatch();
		match.setChallengeAvgDiv1(1);
		match.setChallengeAvgDiv2(2.20f);
		match.setChallengeTotalDiv1(10);
		match.setChallengeTotalDiv2(200);
		match.setCompetitorsDiv1(100);
		match.setCompetitorsDiv2(120);
		match.setCompetitorsTotal(220);
		match.setLink("http://google.com");
		match.setName("Test Match Round 1");
		List<TCProblem> problems = new ArrayList<>();
		{
			TCProblem problem = new TCProblem();
			problem.setName("problem 1");
			problem.setAvgPts(12.1f);

			problem.setCorrectRatio(3.3f);
			problem.setLevel(1);
			problem.setLink("http://link/problems1");
			problem.setStatement("Hello World");
			problem.setSubmission(1003);
			{
				TCProblemClassDefinition pdf = new TCProblemClassDefinition();
				pdf.setDefinitionKey("Class Name");
				pdf.setDefinitionVal("ClassProblem1");
				pdf.setOrder(1);
//				problem.getDefinition().add(pdf);
				pdf = new TCProblemClassDefinition();
				pdf.setDefinitionKey("Signature");
				pdf.setDefinitionVal("def solve(id)");
				pdf.setOrder(2);
//				problem.getDefinition().add(pdf);
			}
			{
				TCProblemExample exp = new TCProblemExample();
				exp.setOrder(1);
				exp.setInput("[1, 2, 5]");
				exp.setExpect("3");
				exp.setNote("the input has 3 elements");
//				problem.getExamples().add(exp);
			}
			{
				TCProblemNote note = new TCProblemNote();
				note.setOrder(1);
				note.setVal("Some notes");
				note.setProblem(problem);
//				problem.getNotes().add(note);
			}
			problems.add(problem);
		}
		match.setProblems(problems);
		match.setTime("2015-06-22");
		Match2Sqlite.persistMatch(match);
	}
}
