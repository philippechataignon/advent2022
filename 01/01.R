input <- c(NA, readLines("01/input.txt"))
input <- as.integer(input)

calories <- integer(0)

inds <- which(is.na(input))
for(i in 2:length(inds)) {
	calories[i-1] <- sum(input[inds[i-1]:inds[i]], na.rm=T)
}

cat("1:", max(calories), "\n")
cat("2:", sum(sort(calories, decreasing=T)[1:3]), "\n")
