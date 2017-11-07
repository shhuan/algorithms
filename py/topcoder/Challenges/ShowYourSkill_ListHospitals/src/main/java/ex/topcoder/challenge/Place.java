package ex.topcoder.challenge;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;
import lombok.ToString;

/**
 * Created by huash06 on 7/2/2015.
 */

@Data
@JsonIgnoreProperties(ignoreUnknown = true)
@ToString(includeFieldNames = true)
public class Place {

    private String name;
    private String address;
    private String uid;
    private PlaceDetail detail_info;
}
