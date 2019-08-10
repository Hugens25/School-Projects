print("***********EX.1***********")
Name <- c("Sam", "Frank", "Amy")
Age <- c(22, 25, 26)
Weight <- c(150, 165, 120)
Sex <- c("M", "M", "F")
df <- data.frame(row.names = Name, Age, Weight, Sex)
print(df)
print("***********EX.2***********")
is.data.frame(mtcars)
print("***********EX.3***********")
mat <- matrix(1:50, nrow = 10)
df2 <- as.data.frame(mat)
print(df2)
print("***********EX.4***********")
df3 <- mtcars
print("df3 <- mtcars")
print("***********EX.5***********")
head(df3, 6)
print("***********EX.6***********")
print(mean(df3$mpg))
print("***********EX.7***********")
print(subset(df3, cyl == 6))
print("***********EX.8***********")
print(df3[c("am", "gear", "carb")])
print("***********EX.9***********")
df3$performance <- round(df3$hp / df3$wt, 2)
head(df3)
print("***********EX.10***********")
#revisedDf <- subset(df3, hp > 100 & wt > 2.5)
#print(revisedDf)
#print(mean(revisedDf$mpg))
print(mean(subset(df3, hp > 100 & wt > 2.5)$mpg))
print("***********EX.11***********")
print(df3["Hornet Sportabout",]$mpg)