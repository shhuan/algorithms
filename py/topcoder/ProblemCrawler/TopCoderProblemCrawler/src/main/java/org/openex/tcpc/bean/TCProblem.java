package org.openex.tcpc.bean;

import com.j256.ormlite.field.DatabaseField;
import com.j256.ormlite.table.DatabaseTable;

@DatabaseTable(tableName = "problem")
public class TCProblem {

	@DatabaseField(generatedId = true)
	private Integer id;

	@DatabaseField(canBeNull = false)
	private String name = "";

	@DatabaseField(canBeNull = false)
	private String link;

	@DatabaseField(canBeNull = true)
	private int level;

	@DatabaseField(canBeNull = true)
	private int div;

	@DatabaseField(canBeNull = true)
	private int submission;

	@DatabaseField(columnName = "correct_ratio", canBeNull = true)
	private float correctRatio;

	@DatabaseField(columnName = "avg_pts", canBeNull = true)
	private float avgPts;

	@DatabaseField(canBeNull = false)
	private String statement;

	@DatabaseField(foreign = true, columnName = "match_id")
	private TCMatch match;

	@DatabaseField
	private String definition;

	@DatabaseField
	private String notes;

	@DatabaseField
	private String constraints;

	@DatabaseField
	private String examples;

	public boolean hasSameLink(TCProblem other){
		return !(this.link == null || other.link == null) && this.link.trim().equalsIgnoreCase(other.link.trim());
	}
	public void copyBasicInfo(TCProblem other){
        if (other == null || other == this) {
            return;
        }
        this.setName(other.getName());
		this.setAvgPts(other.getAvgPts());
		this.setLevel(other.getLevel());
		this.setSubmission(other.getSubmission());
		this.setCorrectRatio(other.getCorrectRatio());
	}
	
	public TCMatch getMatch() {
		return match;
	}

	public void setMatch(TCMatch match) {
		this.match = match;
	}

	public int getLevel() {
		return level;
	}

	public void setLevel(int level) {
		this.level = level;
	}

	public int getSubmission() {
		return submission;
	}

	public void setSubmission(int submission) {
		this.submission = submission;
	}

	public float getAvgPts() {
		return avgPts;
	}

	public void setAvgPts(float avgPts) {
		this.avgPts = avgPts;
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

	public String getStatement() {
		return statement;
	}

	public void setStatement(String statement) {
		this.statement = statement;
	}


	public float getCorrectRatio() {
		return correctRatio;
	}

	public void setCorrectRatio(float correctRatio) {
		this.correctRatio = correctRatio;
	}

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public String getDefinition() {
		return definition;
	}

	public void setDefinition(String definition) {
		this.definition = definition;
	}

	public String getNotes() {
		return notes;
	}

	public void setNotes(String notes) {
		this.notes = notes;
	}

	public String getConstraints() {
		return constraints;
	}

	public void setConstraints(String constraints) {
		this.constraints = constraints;
	}

	public String getExamples() {
		return examples;
	}

	public void setExamples(String examples) {
		this.examples = examples;
	}

	public int getDiv() {
		return div;
	}

	public void setDiv(int div) {
		this.div = div;
	}

	@Override
	public String toString() {
		return "TCProblem [name=" + name + ", link=" + link + ", level=" + level + ", submission=" + submission
				+ ", correct=" + correctRatio + ", avgPts=" + avgPts + ", statement=" + statement + ", definition="
				+ definition + ", notes=" + notes + ", constraints=" + constraints + ", examples=" + examples + "]";
	}

}
