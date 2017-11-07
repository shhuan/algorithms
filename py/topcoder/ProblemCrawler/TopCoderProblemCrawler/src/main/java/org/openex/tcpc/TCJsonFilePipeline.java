package org.openex.tcpc;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.apache.commons.codec.digest.DigestUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import us.codecraft.webmagic.ResultItems;
import us.codecraft.webmagic.Task;
import us.codecraft.webmagic.pipeline.Pipeline;
import us.codecraft.webmagic.utils.FilePersistentBase;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class TCJsonFilePipeline extends FilePersistentBase implements Pipeline {

	final private static Logger logger = LoggerFactory.getLogger(TCJsonFilePipeline.class);

	/**
	 * new JsonFilePageModelPipeline with default path "/data/webmagic/"
	 */
	public TCJsonFilePipeline() {
		PATH_SEPERATOR = "/";
		setPath("/data/webmagic");
	}

	public TCJsonFilePipeline(String path) {
		setPath(path);
	}

	@Override
	public void checkAndMakeParentDirecotry(String fullName) {
        int index = fullName.lastIndexOf("/");
        if (index > 0) {
            String path = fullName.substring(0, index);
            File file = new File(path);
            if (!file.exists()) {
                file.mkdirs();
            }
        }
    }
	
	public void process(ResultItems resultItems, Task task) {
		String path = this.path + "/";
		try {
            FileWriter writer = new FileWriter(getFile(path
                    + DigestUtils.md5Hex(resultItems.getRequest().getUrl()) + ".json"));
            Gson gson = new GsonBuilder().disableHtmlEscaping().setPrettyPrinting().create();
            gson.toJson(resultItems.getAll(), writer);
            writer.close();
        } catch (IOException e) {
			logger.warn("write file error", e);
		}
	}
}
