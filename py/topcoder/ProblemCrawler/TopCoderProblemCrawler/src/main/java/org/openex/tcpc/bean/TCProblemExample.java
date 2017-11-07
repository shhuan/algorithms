package org.openex.tcpc.bean;

import com.j256.ormlite.field.DatabaseField;
import com.j256.ormlite.table.DatabaseTable;

@DatabaseTable(tableName = "problem_example")
public class TCProblemExample {

	@DatabaseField(generatedId = true)
	private int id;

	@DatabaseField(canBeNull = true)
	private int order;

	@DatabaseField(canBeNull = false)
	private String input;

	@DatabaseField(canBeNull = false)
	private String expect;

	@DatabaseField(canBeNull = true)
	private String note;

	@DatabaseField(foreign = true, columnName = "problem_id")
	private TCProblem problem;

	public TCProblem getProblem() {
		return problem;
	}

	public void setProblem(TCProblem problem) {
		this.problem = problem;
	}

	public int getOrder() {
		return order;
	}

	public void setOrder(int order) {
		this.order = order;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getInput() {
		return input;
	}

	public void setInput(String input) {
		this.input = input;
	}

	public String getExpect() {
		return expect;
	}

	public void setExpect(String expect) {
		this.expect = expect;
	}

	public String getNote() {
		return note;
	}

	public void setNote(String note) {
		this.note = note;
	}

	@Override
	public String toString() {
		return "TCProblemExample [id=" + id + ", input=" + input + ", expect=" + expect + ", note=" + note + "]";
	}

}
