int countLettersAndDigits(std::string input)
{
    int count = 0;
    for (int i = 0; i < input.size(); i++){
      if (isalpha(input[i]) || isdigit(input[i])){
        count = count + 1;
      }
    }
    return count;
}
