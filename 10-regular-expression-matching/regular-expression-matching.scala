object Solution {
  
  def isMatch(s: String, p: String): Boolean = {
    val m = s.length
    val n = p.length
    
    // dp[i][j] represents if s[0...i-1] matches p[0...j-1]
    val dp = Array.ofDim[Boolean](m + 1, n + 1)
    
    // Empty pattern matches empty string
    dp(0)(0) = true
    
    // Handle patterns like a*, a*b*, a*b*c* etc.
    for (j <- 1 to n) {
      if (p(j - 1) == '*' && j > 1) {
        dp(0)(j) = dp(0)(j - 2)
      }
    }
    
    // Fill the dp table
    for (i <- 1 to m; j <- 1 to n) {
      if (p(j - 1) == '*') {
        // Case 1: Zero occurrence of char before *
        dp(i)(j) = dp(i)(j - 2)
        
        // Case 2: One or more occurrences of char before *
        if (p(j - 2) == '.' || p(j - 2) == s(i - 1)) {
          dp(i)(j) = dp(i)(j) || dp(i - 1)(j)
        }
      } else if (p(j - 1) == '.' || p(j - 1) == s(i - 1)) {
        // Current characters match
        dp(i)(j) = dp(i - 1)(j - 1)
      }
    }
    
    dp(m)(n)
  }
}
