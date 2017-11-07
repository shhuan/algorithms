package ex.topcoder.challenge;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;
import lombok.ToString;

import java.util.List;

/**
 * Created by huash06 on 7/2/2015.
 */
@Data
@JsonIgnoreProperties(ignoreUnknown = true)
@ToString(includeFieldNames = true)

public class PlaceResponse {
    private int status;
    private List<Place> results;
}
