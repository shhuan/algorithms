package open.ex.zoj.sim.p1116;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
	public static boolean ONLINE_JUDGE = true;

	public static void main(String[] args) {
		if (!ONLINE_JUDGE) {
			System.setIn(Main.class.getClassLoader().getResourceAsStream("input_1116.txt"));
		}

		Scanner scanner = new Scanner(System.in);

		String startTag = null;
		do {
			startTag = scanner.nextLine();
		} while (scanner.hasNextLine() && !startTag.equals("<?xml version=\"1.0\"?>"));
		while (true) {
			String line = null;
			StringBuilder textBuilder = new StringBuilder();
			while (true) {
				line = scanner.nextLine();
				if (line.equals("<?xml version=\"1.0\"?>") || line.equals("<?end?>")) {
					break;
				}
				textBuilder.append(line);
			}
			if (check(textBuilder.toString())) {
				System.out.println("well-formed");
			} else {
				System.out.println("non well-formed");
			}
			if (line.equals("<?end?>")) {
				break;
			}
		}
		scanner.close();
	}

	private static boolean check(String text) {
		/*
		 * 1. There is exactly one element that is not contained within any
		 * other element. This element is identified as the "root" or "document"
		 * element. In the example above, "customer" is the document element.
		 */
		if (!text.matches("\\s*<([\\w-]+)(\\s+[^\\s]+)*>.*</\\1>\\s*")) {
			// System.out.println("Text doesn't match rule #1");
			return false;
		}
		return parseText(text);
	}

	private static boolean parseText(String text) {
		if (text == null || text.length() <= 0 || text.matches("[^<>]+")) {
			return true;
		}
		int tagStart = text.indexOf('<');
		int tagEnd = text.indexOf('>');

		String strBeforeTag = text.substring(0, tagStart);
		if (strBeforeTag != null && strBeforeTag.length() > 0 && !strBeforeTag.matches("[^<>]+")) {
			// System.out.println("=================#1========================");
			// System.out.println(text);
			// System.out.println("=================#1========================");
			return false;
		}

		String tag = null;
		if (text.charAt(tagEnd - 1) == '/') {
			tag = parseTag(text.substring(tagStart + 1, tagEnd - 1));
			if (tag == null || tag.length() <= 0) {
				// System.out.println("=================#3========================");
				// System.out.println(text);
				// System.out.println("=================#3========================");
				return false;
			}
			return parseText(text.substring(tagEnd + 1));
		}

		tag = parseTag(text.substring(tagStart + 1, tagEnd));
		if (tag == null || tag.length() <= 0) {
			return false;
		}
		int contentStart = tagEnd + 1;
		/*
		 * 5. A parsed element must not contain a recursive reference to itself.
		 * For example, it is improper to include another address element within
		 * an address element.
		 * 
		 * Directly search next </tag> can ensure this, because if there is an
		 * recursive refer like: <tag> <tag> </tag> </tag> the {tagENd} will
		 * point to the first </tag> and the remainder texts are not well-formed
		 */
		int contentEnd = text.indexOf("</" + tag + ">");

		/*
		 * 2. The structure of an XML document must nest properly. An element's
		 * start-tag must be paired with a closing end-tag if it is a non-empty
		 * element.
		 * 
		 * 3. The name in an element's end-tag must match the element type in
		 * the start-tag. For example, an element opened with <address> must be
		 * closed by </address>.
		 */
		if (contentEnd < 0) {
			// System.out.println("=================#2========================");
			// System.out.println(text);
			// System.out.println("=================#2========================");
			return false;
		}

		if (!parseText(text.substring(contentStart, contentEnd))) {
			return false;
		}

		String strAfterTag = text.substring(contentEnd + tag.length() + 3);
		if (strAfterTag != null && strAfterTag.length() > 0) {
			return parseText(strAfterTag);
		}
		return true;
	}

	/**
	 * @param tag
	 *            item attr="some val"
	 * @return tag name or null if input tag is invalid
	 */
	private static String parseTag(String tag) {

		/*
		 * 6. A named attribute must have an associated value. This is ensured
		 * by (\\s+\\w+\\s*=\\s*\".+\")
		 */
		Pattern p = Pattern.compile("([\\w-]+)(\\s+[\\w-]+\\s*=\\s*\".+\")*\\s*");
		Matcher matcher = p.matcher(tag);
		if (!matcher.matches()) {
			// System.out.println("=================#6========================");
			// System.out.println(tag);
			// System.out.println("=================#6========================");
			return null;
		}
		String tagName = matcher.group(1);

		String[] attrs = tag.substring(tag.indexOf(tagName) + tagName.length()).split("=");
		Set<String> attrNames = new HashSet<>();
		for (int i = 0; i < attrs.length; i += 2) {
			String attr = attrs[i].trim();
			/*
			 * 4. No attribute may appear more than once in the same start-tag
			 * or empty-element tag.
			 */
			if (attrNames.contains(attr)) {
				// System.out.println("=================#4========================");
				// System.out.println(tag);
				// System.out.println("=================#4========================");
				return null;
			}
			attrNames.add(attrs[i].trim());
		}

		return tagName;
	}

}
