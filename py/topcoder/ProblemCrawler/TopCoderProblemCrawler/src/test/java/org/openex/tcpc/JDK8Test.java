package org.openex.tcpc;

import org.junit.Assert;
import org.junit.Test;
import org.openex.tcpc.bean.TCMatch;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by huash06 on 6/29/2015.
 */
public class JDK8Test {


    @Test
    public void testStream(){
        TCMatch match = new TCMatch();
        match.setName("test");
        match.setLink("http://www.test.com/m1");

        List<TCMatch> matchBasicInfos = new ArrayList<>();
        TCMatch m1 = new TCMatch();
        m1.setName("m1");
        m1.setLink("hhhhh");

        TCMatch m2 = new TCMatch();
        m2.setName("m2");
        m2.setLink("http://www.test.com/m1");

        matchBasicInfos.add(m1);
        matchBasicInfos.add(m2);
        System.out.println(matchBasicInfos.stream().filter(s -> s.hasSameLink(match)).findFirst().get());
    }

    @Test
    public void regularExpressionTest() {
        Assert.assertEquals("some text", "<table>some text</ssa>".replaceAll("^<[^<>]*>", "").replaceAll("</[^<>]*>$", ""));

    }
}
