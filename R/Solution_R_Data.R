# Import jsonlite package
library(jsonlite)
library(stringr)

# There are two ways to load data and parse it as dataframe

#  1
# load the input file into memory one time, than using some transformations on matrix
# and aggregated operations such as "sapply" to build the dataframe.
loadDataOneTime <- function(){
  oldpath <- getwd()
  datapath <- "review.data"
  # load the data into the memory one time
  lines <- readLines(datapath) 
  # convert JSON entry into a dataframe
  jsonData <- as.data.frame(t(sapply(lines, fromJSON)))
  # Remove the dataframe row name
  rownames(jsonData) <- c()
  jsonData <- transform(jsonData, overall = as.numeric(overall))
  setwd(oldpath)
  return(jsonData)
}

# 2
# Using I/O APIs in R to read the input file line by line, after reading 
# a line from the file, you can invoke some APIs (maybe from "rjson" or "jsonlite") 
# to convert this JSON entry into R intermediate data. Finally you can combine all 
# intermediate into a dataframe. 
loadDataByLine <- function(){
  oldpath <- getwd()
  filepath <- "review.data"
  
  # Open the input file with readonly
  con = file(filepath, "r")
  
  # Define an empty dataframe with 
  # specific type info for each column
  df <- data.frame(reviewerID=character(),
                   asin=character(),
                   reviewTex=character(),
                   overall=double(),
                   reviewTime=character())
  
  # Read one line from the open file "con",
  # then the file pointer will point to next line
  line <- readLines(con = con,n = 1)
  
  while(length(line) != 0){
    # Convert a JSON entry into a dataframe
    data <- as.data.frame(fromJSON(line))
    
    # append it into df 
    df <- rbind(df,data)
    
    # Get next line data
    line <- readLines(con = con,n = 1)
  }
  
  # Close the input file
  close(con)
  setwd(oldpath)
  return(df)
}

input <- loadDataOneTime()
output <- input[input$overall >= 4, ]