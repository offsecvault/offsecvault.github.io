rule pdf_file_easy
{
meta:
  author: "b0ydC"
  description: "basic YARA rule to detect .pdf files"
  
strings:
  $start = "%PDF"
  $end = "%%EOF"
  
condition:
  $start at 0 and $end
}
