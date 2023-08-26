// This solution beat 67.35% in runtime and 85.97% in memory usage of all C# submissions :)
// This was my first submission and I published to leetcode

public class Solution {
    public bool CanConstruct(string ransomNote, string magazine) {
        // Build a freq dictionary of the letters in magazine
        var mDict = new Dictionary<char, int>();
        foreach ( char c in magazine ) {
            if ( mDict.ContainsKey(c) ) mDict[c]++;
            else mDict[c] = 1;
        }
        // Loop through ransom note and for each letter, see if it can be "pulled" from the freq dict
        foreach ( char c in ransomNote ) {
            if ( mDict.TryGetValue(c, out int numLeft) ) {
                if ( numLeft > 0 ) mDict[c]--;
                else return false;
            } else {
                return false;
            }
        }
        return true;
    }
}


// here is a slight improvement I noticed from another solution in runtime complexity by using less comparisons

public class Solution {
    public bool CanConstruct(string ransomNote, string magazine) {
        // Build a freq dictionary of the letters in magazine
        var mDict = new Dictionary<char, int>();
        foreach ( char c in magazine ) {
            if ( mDict.ContainsKey(c) ) mDict[c]++;
            else mDict[c] = 1;
        }
        // Loop through ransom note and for each letter, see if it can be "pulled" from the freq dict
        foreach ( char c in ransomNote ) {
            if ( !mDict.ContainsKey(c) ) return false;
            else {
                mDict[c]--;
                if ( mDict[c] == 0 ) mDict.Remove(c);
            }
        }
        return true;
    }
}
