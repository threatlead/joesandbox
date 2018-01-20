# ![JoeSandbox](https://s13.postimg.org/mex3nuox3/debug.png) Joe Sandbox Parser

## Usage

### Recent Analysis

```python
import joesandbox
print(joesandbox.JoeSandbox.recent_analysis())
```

```javascript
[43162, 43161, 43160, 43159, 43158, 43157, 43156, 43155, 43154, 43153, 43152, 43151, 43150, 43149, 43148, 43147, 43146, 43145, 43144, 43143]
```

### Analysis Report (uses `xmltodict`)

```python
print(joesandbox.JoeSandbox.get_analysis(joe_id=43162))
```

```javascript
OrderedDict([
   ('analysis',
   OrderedDict(   [
      ('version',
      '20.0.0'      ),
      ('reporttype',
      'IR'      ),
      ('errors',
      None),
      ('id',
      '43162'      ),
      ('starttime',
      '00:09:03'      ),
      ('startdate',
      '20/01/2018'      ),
      ('sample',
      'resume.doc'      ),
      ('cookbook',
      'defaultwindowsofficecookbook.jbs'      ),
      ('system',
      'Windows 7 SP1 (with Office 2010 SP2, IE 11, FF 54, Chrome 60, Acrobat Reader DC 17, Flash 26, Java 8.0.1440.1)'      ),
      ('arch',
      'WINDOWS'      ),
      ('hashes',
      OrderedDict(      [
         ('md5',
         '51c374cb04be9298983a5069edbebc7c'         ),
         ('sha1',
         'ea8e9a33ce21a267f11d9e39030bd97a42a8b595'         ),
         ('sha256',
         '82eb448f9f995a3a1ebaf6fcde70bd0c529ffe9b47d2584ebf08069710a2a458'         )
      ]      )),
      ('filetype',
      'Microsoft Word document (32009/1) 48.12%'      ),
      ('detection',
      OrderedDict(      [
         ('malicious',
         'true'         ),
         ('suspicious',
         'false'         ),
         ('clean',
         'false'         ),
         ('unknown',
         'false'         ),
         ('score',
         '80'         ),
         ('minscore',
         '0'         ),
         ('maxscore',
         '100'         )
      ]      )),
      ('confidence',
      OrderedDict(      [
         ('score',
         '5'         ),
         ('minscore',
         '0'         ),
         ('maxscore',
         '5'         ),
         ('expertadviceneeded',
         'false'         )
      ]      )),
      ('dropped',
      OrderedDict(      [
         ('@isArray',
         'true'         ),
         ('file',
         [
            OrderedDict(            [
               ('name',
               'C:\\Users\\user\\AppData\\Local\\Microsoft\\Windows\\Temporary Internet Files\\Content.Word\\~WRS{F99ECEA7-6475-4D26-8682-77BF148D15F5}.tmp'               ),
               ('malicious',
               'false'               ),
               ('md5',
               '5D4D94EE7E06BBB0AF9584119797B23A'               ),
               ('sha1',
               'DBB111419C704F116EFA8E72471DD83E86E49677'               ),
               ('sha256',
               '4826C0D860AF884D3343CA6460B0006A7A2CE7DBCCC4D743208585D997CC5FD1'               )
            ]            ),
            OrderedDict(            [
               ('name',
               'C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Office\\Recent\\index.dat'               ),
               ('malicious',
               'false'               ),
               ('md5',
               '86148D81B25B6A156FF83528C0C623B2'               ),
               ('sha1',
               'C7FFC33831987EACADA4A7BA0A6DEF9B398A5F16'               ),
               ('sha256',
               '558D8AF9DDF9026F0B40D9529F43DB7029B7B12A81585F6A68E15F1151E4A1E6'               )
            ]            ),
            OrderedDict(            [
               ('name',
               'C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Office\\Recent\\resume.LNK'               ),
               ('malicious',
               'false'               ),
               ('md5',
               'CD3E1EA707AF7EF37D82E72042615FAB'               ),
               ('sha1',
               '08718D09B86FA96C6BAC500674764FD8C5614415'               ),
               ('sha256',
               '6C76B7BF892AFE0F2D0B7C4C3C0759E88EB5FB950A0DEAB4736DA6E8111F1987'               )
            ]            ),
            OrderedDict(            [
               ('name',
               'C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Templates\\~$Normal.dotm'               ),
               ('malicious',
               'false'               ),
               ('md5',
               'FF291ADF1F74826EE3AA31EA36ADEC1C'               ),
               ('sha1',
               '9E647BCB57789C91D08C9B02D73ECD048239B5C5'               ),
               ('sha256',
               '08B022FE12FDA6C82FEEA4C0B2736E6FF757EA90DFF28CE43E7D44CD5FB4AE36'               )
            ]            ),
            OrderedDict(            [
               ('name',
               'C:\\Users\\user\\Desktop\\~$resume.doc'               ),
               ('malicious',
               'true'               ),
               ('md5',
               'FF291ADF1F74826EE3AA31EA36ADEC1C'               ),
               ('sha1',
               '9E647BCB57789C91D08C9B02D73ECD048239B5C5'               ),
               ('sha256',
               '08B022FE12FDA6C82FEEA4C0B2736E6FF757EA90DFF28CE43E7D44CD5FB4AE36'               )
            ]            )
         ]         )
      ]      )),
      ('contacted',
      OrderedDict(      [
         ('ips',
         OrderedDict(         [
            ('@isArray',
            'true'            ),
            ('ip',
            OrderedDict(            [
               ('@malicious',
               'true'               ),
               ('#text',
               '80.82.67.21'               )
            ]            ))
         ]         )),
         ('domains',
         OrderedDict(         [
            ('@isArray',
            'true'            )
         ]         ))
      ]      )),
      ('signatures',
      OrderedDict(      [
         ('signare',
         [
            'Document contains an embedded VBA macro which executes code when the document is opened / closed',
            'Document contains an embedded VBA macro which may execute processes',
            'Document contains an embedded VBA macro with suspicious strings',
            'Document contains an embedded VBA with base64 encoded strings',
            'Document contains an embedded VBA with many string operations indicating source code obfuscation',
            'Document exploit detected (process start blacklist hit)',
            'Obfuscated command line found',
            'Tries to download files via bitsadmin',
            'Antivirus detection for submitted file'
         ]         )
      ]      ))
   ]   ))
])
```