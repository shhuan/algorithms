package org.openex.tcpc.bean;

import com.j256.ormlite.field.DatabaseField;
import com.j256.ormlite.table.DatabaseTable;

import java.util.ArrayList;
import java.util.List;

@DatabaseTable(tableName = "match")
public class TCMatch {

	@DatabaseField(generatedId = true)
	private Integer id;

	@DatabaseField(canBeNull = false)
	private String name;

	@DatabaseField(canBeNull = false)
	private String link;

	@DatabaseField(canBeNull = false)
	private String time;

	@DatabaseField(columnName = "competitors_total", canBeNull = true)
	private int competitorsTotal;

	@DatabaseField(columnName = "competitors_div1", canBeNull = true)
	private int competitorsDiv1;

	@DatabaseField(columnName = "competitors_div2", canBeNull = true)
	private int competitorsDiv2;

	@DatabaseField(columnName = "submission_total_div1", canBeNull = true)
	private int submissionTotalDiv1;

	@DatabaseField(columnName = "submission_avg_div1", canBeNull = true)
	private float submissionAvgDiv1;

	@DatabaseField(columnName = "challenge_total_div1", canBeNull = true)
	private int challengeTotalDiv1;

	@DatabaseField(columnName = "challenge_avg_div1", canBeNull = true)
	private float challengeAvgDiv1;

	@DatabaseField(columnName = "submission_total_div2", canBeNull = true)
	private int submissionTotalDiv2;

	@DatabaseField(columnName = "submission_avg_div2", canBeNull = true)
	private float submissionAvgDiv2;

	@DatabaseField(columnName = "challenge_total_div2", canBeNull = true)
	private int challengeTotalDiv2;

	@DatabaseField(columnName = "challenge_avg_div2", canBeNull = true)
	private float challengeAvgDiv2;

	private List<TCProblem> problems = new ArrayList<>();

	public boolean hasSameLink(TCMatch other) {
		return !(this.link == null || other.link == null) && this.link.trim().equalsIgnoreCase(other.link.trim());
	}

	public void copyBasicInfo(TCMatch other) {
		this.time = other.time;
		this.competitorsTotal = other.competitorsTotal;
		this.competitorsDiv1 = other.competitorsDiv1;
		this.competitorsDiv2 = other.competitorsDiv2;
		this.submissionTotalDiv1 = other.submissionTotalDiv1;
		this.submissionTotalDiv2 = other.submissionTotalDiv2;
		this.submissionAvgDiv1 = other.submissionAvgDiv1;
		this.submissionAvgDiv2 = other.submissionAvgDiv2;
		this.challengeAvgDiv1 = other.challengeAvgDiv1;
		this.challengeAvgDiv2 = other.challengeAvgDiv2;
		this.challengeTotalDiv1 = other.challengeTotalDiv1;
		this.challengeTotalDiv2 = other.challengeTotalDiv2;
	}

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getLink() {
		return link;
	}

	public void setLink(String link) {
		this.link = link;
	}

	public String getTime() {
		return time;
	}

	public void setTime(String time) {
		this.time = time;
	}

	public int getCompetitorsTotal() {
		return competitorsTotal;
	}

	public void setCompetitorsTotal(int competitorsTotal) {
		this.competitorsTotal = competitorsTotal;
	}

	public int getCompetitorsDiv1() {
		return competitorsDiv1;
	}

	public void setCompetitorsDiv1(int competitorsDiv1) {
		this.competitorsDiv1 = competitorsDiv1;
	}

	public int getCompetitorsDiv2() {
		return competitorsDiv2;
	}

	public void setCompetitorsDiv2(int competitorsDiv2) {
		this.competitorsDiv2 = competitorsDiv2;
	}

	public int getSubmissionTotalDiv1() {
		return submissionTotalDiv1;
	}

	public void setSubmissionTotalDiv1(int submissionTotalDiv1) {
		this.submissionTotalDiv1 = submissionTotalDiv1;
	}

	public float getSubmissionAvgDiv1() {
		return submissionAvgDiv1;
	}

	public void setSubmissionAvgDiv1(float submissionAvgDiv1) {
		this.submissionAvgDiv1 = submissionAvgDiv1;
	}

	public int getChallengeTotalDiv1() {
		return challengeTotalDiv1;
	}

	public void setChallengeTotalDiv1(int challengeTotalDiv1) {
		this.challengeTotalDiv1 = challengeTotalDiv1;
	}

	public float getChallengeAvgDiv1() {
		return challengeAvgDiv1;
	}

	public void setChallengeAvgDiv1(float challengeAvgDiv1) {
		this.challengeAvgDiv1 = challengeAvgDiv1;
	}

	public int getSubmissionTotalDiv2() {
		return submissionTotalDiv2;
	}

	public void setSubmissionTotalDiv2(int submissionTotalDiv2) {
		this.submissionTotalDiv2 = submissionTotalDiv2;
	}

	public float getSubmissionAvgDiv2() {
		return submissionAvgDiv2;
	}

	public void setSubmissionAvgDiv2(float submissionAvgDiv2) {
		this.submissionAvgDiv2 = submissionAvgDiv2;
	}

	public int getChallengeTotalDiv2() {
		return challengeTotalDiv2;
	}

	public void setChallengeTotalDiv2(int challengeTotalDiv2) {
		this.challengeTotalDiv2 = challengeTotalDiv2;
	}

	public float getChallengeAvgDiv2() {
		return challengeAvgDiv2;
	}

	public void setChallengeAvgDiv2(float challengeAvgDiv2) {
		this.challengeAvgDiv2 = challengeAvgDiv2;
	}

	public List<TCProblem> getProblems() {
		return problems;
	}

	public void setProblems(List<TCProblem> problems) {
		this.problems = problems;
	}

	@Override
	public String toString() {
		return "TCMatch [name=" + name + ", link=" + link + ", time=" + time + ", competitorsTotal=" + competitorsTotal
				+ ", competitorsDiv1=" + competitorsDiv1 + ", competitorsDiv2=" + competitorsDiv2
				+ ", submissionTotalDiv1=" + submissionTotalDiv1 + ", submissionAvgDiv1=" + submissionAvgDiv1
				+ ", challengeTotalDiv1=" + challengeTotalDiv1 + ", challengeAvgDiv1=" + challengeAvgDiv1
				+ ", submissionTotalDiv2=" + submissionTotalDiv2 + ", submissionAvgDiv2=" + submissionAvgDiv2
				+ ", challengeTotalDiv2=" + challengeTotalDiv2 + ", challengeAvgDiv2=" + challengeAvgDiv2
				+ ", problems=" + problems + "]";
	}

}
