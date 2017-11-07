package org.openex.tcpc.bean;

import java.util.ArrayList;
import java.util.List;

public class TCMatchArchive {

    private List<TCMatch> matches = new ArrayList<>();

    public List<TCMatch> getMatches() {
        return matches;
    }

    public void setMatches(List<TCMatch> matches) {
        this.matches = matches;
    }


}
