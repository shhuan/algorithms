package ex.topcoder.challenge;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;
import lombok.ToString;

/**
 * Created by huash06 on 7/2/2015.
 */

@Data
@ToString
@JsonIgnoreProperties(ignoreUnknown = true)
public class PlaceDetail {
    private String detail_url;
    private String image_url;
}
