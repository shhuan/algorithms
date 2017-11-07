package org.openex.tcpc.bean;

import com.j256.ormlite.field.DatabaseField;
import com.j256.ormlite.table.DatabaseTable;

@DatabaseTable(tableName = "problem_constraint")
public class TCProblemConstraint {

	@DatabaseField(generatedId = true)
	private Integer id;

	@DatabaseField(canBeNull = true, defaultValue = "0")
	private int order;

	@DatabaseField(canBeNull = false)
	private String val;

	@DatabaseField(foreign = true, columnName = "problem_id")
	private TCProblem problem;

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public int getOrder() {
		return order;
	}

	public void setOrder(int order) {
		this.order = order;
	}

	public String getVal() {
		return val;
	}

	public void setVal(String val) {
		this.val = val;
	}

	public TCProblem getProblem() {
		return problem;
	}

	public void setProblem(TCProblem problem) {
		this.problem = problem;
	}

	@Override
	public String toString() {
		return "TCProblemConstraint [order=" + order + ", val=" + val + "]";
	}

}
