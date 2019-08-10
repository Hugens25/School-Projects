# Hugens Ulysse R Data

# I wasn't sure if i was only supposed to print the review text, or if
# you wanted the entire row of data printed to ensure the correct data
# was printed out. So here, I print out the entire row, but I also included
# the code below which shows how I would modify my code if I were to only
# extract the reviewText of reviews whose overall rating >= 4.

library(rjson)
library(stringr)
library(gridExtra)

cat("\n\nGetting all reviews with ratings greater than 4.\n\n")
cat("The printed output may take a few seconds to complete..\n\n")

data <- readLines("review.data")
review <- as.data.frame(t(sapply(data,fromJSON)))
rownames(review) <- c()
reviews_4plus <- subset(review, overall >= 4.0)
print.data.frame(reviews_4plus)
#print(reviews_4plus)$reviewText
