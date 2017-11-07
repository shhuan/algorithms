package org.openex.tcpc.bean;

import com.j256.ormlite.field.DatabaseField;
import com.j256.ormlite.table.DatabaseTable;

@DatabaseTable(tableName = "problem_definition")
public class TCProblemClassDefinition {

    @DatabaseField(generatedId = true)
    private Integer id;

    @DatabaseField(canBeNull = false)
    private int order;

    @DatabaseField(columnName = "def_key", canBeNull = true)
    private String definitionKey;

    @DatabaseField(columnName = "def_val", canBeNull = true)
    private String definitionVal;

    @DatabaseField(foreign = true, columnName = "problem_id")
    private TCProblem problem;

    public TCProblem getProblem() {
        return problem;
    }

    public void setProblem(TCProblem problem) {
        this.problem = problem;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getDefinitionKey() {
        return definitionKey;
    }

    public void setDefinitionKey(String definitionKey) {
        this.definitionKey = definitionKey;
    }

    public String getDefinitionVal() {
        return definitionVal;
    }

    public void setDefinitionVal(String definitionVal) {
        this.definitionVal = definitionVal;
    }

    public int getOrder() {
        return order;
    }

    public void setOrder(int order) {
        this.order = order;
    }

    @Override
    public String toString() {
        return "TCProblemClassDefinition [id=" + id + ", definitionKey=" + definitionKey + ", definitionVal="
                + definitionVal + "]";
    }

}
