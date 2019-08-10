df <- read.csv(file="test3data.csv", header=TRUE, sep=",")
df <- subset(df, Industry != "")
for (row in 1:nrow(df)) {
  if(df[row, "City"] == "Jackson" & df[row, "State"] == ""){
    df[row, "State"] <- "Mississippi"
  }
  if(df[row, "City"] == "Cheyenne" & df[row, "State"] == ""){
    df[row, "State"] <- "Wyoming"
  }
  if(df[row, "City"] == "Sacramento" & df[row, "State"] == ""){
    df[row, "State"] <- "California"
  }
  # if(df[row, "Revenue"] == ""){
  #   df[row, "Revenue"] <- mean(df$Revenue)
  # }
  # if(df[row, "Expenses"] == ""){
  #   df[row, "Expenses"] <- mean(df$Expenses)
  # }
   # if(df[row, "Profit"] == "NA"){
   #   df[row, "Profit"] <- mean(df$Profit, na.rm = TRUE)
   # }
}

print("********** Mean of Month 6 Below **********")
print(median(subset(df, Month == 6)$Profit, na.rm = TRUE))


#**********************PROBLEM 2************************
data <- read.csv("cherry.csv")
my.plot <- barplot(data$Height, data$Volume, main="Height vs Volume", ylab="Height", xlab="Volume")
print("********** Description of Plot Below **********")
summary(my.plot)
