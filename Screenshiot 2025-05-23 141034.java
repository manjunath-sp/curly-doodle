class Solution {
    public int solution(int A) {
        String stringVal = String.valueOf(A);
        char[] digits = stringVal.toCharArray();

        for (int k = 0; k < digits.length; k++) {
            if (digits[k] == '6') {
                digits[k] = '9';
                return Integer.parseInt(new String(digits));
            }
        }
        return A;
    }
}