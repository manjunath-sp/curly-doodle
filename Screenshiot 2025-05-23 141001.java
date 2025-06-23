import java.util.Arrays;

class Solution {
  public int solution(String letters) {
    int[] lowerCaseCharIndex = new int[26];
    Arrays.fill(lowerCaseCharIndex, -1);
    
    int[] firstUpperIndex = new int[26];
    Arrays.fill(firstUpperIndex, Integer.MAX_VALUE);
    
    for (int i = 0; i < letters.length(); i++) {
      char charAt = letters.charAt(i);

      if (Character.isLowerCase(charAt)) {
        int charIndex = charAt - 'a';
        lowerCaseCharIndex[charIndex] = i;
      } else if (Character.isUpperCase(charAt)) {
        int charIndex = charAt - 'A';
        firstUpperIndex[charIndex] = Math.min(firstUpperIndex[charIndex], i);
      }
    }
    int count = 0;
    for (int j = 0; j < 26; j++) {
      boolean hasLowercase = (lowerCaseCharIndex[j] != -1);
      boolean hasUppercase = (firstUpperIndex[j] != Integer.MAX_VALUE);
      if (hasLowercase && hasUppercase) {
        if (lowerCaseCharIndex[j] < firstUpperIndex[j]) {
          count++;
        }
      }
    }
    return count;
  }
  
}