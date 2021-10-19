rule MIRRORBLAST_REBOL_RULE {

meta:

author = "b0ydC"
description = "yara rule to detect mirrorblast rebol .msi variant"
date = "10/18/2021"    
version = "v1.0"
ref = "https://bazaar.abuse.ch/sample/a69d27abd043cc676095f71300bf6b2368167536fcd4fe5342cf79a7e94fc2fe/"

strings:

$folder = "ChromeTempFolder"
$software= "rebol_view_278_3_1.exe"
$wininstallXMLtoolset= "(3.11.0.1528)"

condition:

any of them

}
