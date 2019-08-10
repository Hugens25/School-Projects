# Hugens Ulysse R Analytics
#install.packages("gridExtra", repos = "http://cran.univ-lyon1.fr")

library(rjson)
library(stringr)
Lines <- readLines("review.data")
review <- as.data.frame(t(sapply(Lines,fromJSON)))
rownames(review) <- c()
review["numWords"] <- NA
row <- NROW(review)
nwords <- function(string, pseudo=F){
  ifelse( pseudo,
          pattern <- "\\S+",
          pattern <- "[[:alpha:]]+"
  )
  str_count(string, pattern)
}
for (i in 1:row)
{
  review$numWords[i] <- nwords(review$reviewText[i], F)
}
levels <- c(0,0,0,0,0)
for (i in 1:5)
{
  x <- c(review$numWords[review$overall == i])
  levels[i] <- mean(x)
}
print(levels)
plot(levels,xlab='Overall',ylab='Average Number of Words'))
