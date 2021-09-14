rule doc_file_easy
{
meta:
  author = "b0ydC"
  description = "basic YARA rule to detect .doc files"
  date = "09/13/2021"
  
strings:
  $start = "bjbj8"
  $end = "Word.Document.8"
  
condition:
  $start at 0 and $end
}

// add more strings as you needs and remember to modify the condition.
