class Solution {
    public int solution(String S) {
        int length = S.length();
        int count = 0;
        char[] charArray = S.toCharArray();

        for (int i = 0; i < length; i++) {
            char firstChar = charArray[i];
            char lastChar = charArray[(i - 1 + length) % length];
            if (firstChar == lastChar) {
                count++;
            }
        }
        return count;
    }
}