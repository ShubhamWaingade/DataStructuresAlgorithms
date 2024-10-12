class Solution {
    public boolean isAlienSorted(String[] words, String order){
        HashMap<Character, Integer> orderMap = new HashMap<>();

        for (int index = 0; index < order.length(); index++) {
            orderMap.put(order.charAt(index), index);
        }

        for (int ind = 0; ind < words.length - 1; ind++) {
            for (int innerInd = 0; innerInd < words[ind].length(); innerInd++) {
                if(innerInd >= words[ind+1].length()){
                    return false;
                }
                if(words[ind].charAt(innerInd) != words[ind+1].charAt(innerInd)){
                    int currentWordLetterOrder = orderMap.get(words[ind].charAt(innerInd));
                    int nextWordLetterOrder = orderMap.get(words[ind+1].charAt(innerInd));
                    
                    if(nextWordLetterOrder < currentWordLetterOrder){
                        return false;
                    }else{
                        break;
                    }
                }
            }
        }
        return true;
    }
}