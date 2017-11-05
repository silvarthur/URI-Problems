import java.util.Scanner;

public class Problem1168 {
	public static void main(String[] args) {

		int[] numberOfLedsByNum = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

		Scanner scn = new Scanner(System.in);

		String n = scn.nextLine();

		for(int i = 0; i < Integer.parseInt(n); i++) {
			int output = 0;
			String value = scn.nextLine();
			
			for(int j = 0; j < value.length(); j++) {
				output += numberOfLedsByNum[Integer.parseInt(value.split("")[j])];
			}

			System.out.printf("%d leds" + "\n", output);
		}
	}
}