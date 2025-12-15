# TRS-80 Model 100 BASIC Reference
Extracted from `basic_docs` (keywordDataset.json) for quick navigation.

<a id="index"></a>
## Index
- ['](#kw-symbol-0)
- [*](#kw-symbol-1)
- [+](#kw-symbol-2)
- [-](#kw-symbol-3)
- [/](#kw-symbol-4)
- [<](#kw-symbol-5)
- [=](#kw-symbol-6)
- [>](#kw-symbol-7)
- [ABS](#kw-abs) - Absolute value
- [AND](#kw-and) - Logical AND
- [ASC](#kw-asc) - ASCII code of first character
- [ATN](#kw-atn) - Arctangent
- [BEEP](#kw-beep) - Emit a Tone
- [CALL](#kw-call) - Call a Machine Level Subroutine
- [CDBL](#kw-cdbl) - Convert to Double-Precision
- [CHR$](#kw-chr) - Character Value
- [CINT](#kw-cint) - Convert to Integer
- [CLEAR](#kw-clear) - Clear Variables and Allocate String Space
- [CLOAD](#kw-cload) - Load a Program From Cassette
- [CLOSE](#kw-close) - Close Open Files
- [CLS](#kw-cls) - Clear Screen
- [COM](#kw-com) - Enable/Disable Communications Interrupt
- [CONT](#kw-cont) - Continue Execution
- [COS](#kw-cos) - Cosine
- [CSAVE](#kw-csave) - Save a Program on Cassette
- [CSNG](#kw-csng) - Convert to Single Precision
- [CSRLIN](#kw-csrlin) - Vertical Cursor Position
- [DATA](#kw-data) - Define a Data Set
- [DATE$](#kw-date) - Current Date
- [DAY$](#kw-day) - Current Day of Week
- [DEF](#kw-def)
- [DIM](#kw-dim) - Define Array Size
- [DSKI$](#kw-dski)
- [DSKO$](#kw-dsko)
- [EDIT](#kw-edit) - Edit a BASIC Program
- [ELSE](#kw-else) - Used with IF to specify false branch
- [END](#kw-end) - End Execution
- [EOF](#kw-eof) - Test for End-of-File
- [EQV](#kw-eqv)
- [ERL](#kw-erl) - Get Line Number of Error
- [ERR](#kw-err) - Get Error Code Number
- [ERROR](#kw-error) - Simulate an Error
- [EXP](#kw-exp) - Exponential (Antilog)
- [FILES](#kw-files) - Display File Names
- [FIX](#kw-fix) - Truncate Real Numbers
- [FOR](#kw-for) - Establish Program Looping
- [FRE](#kw-fre) - Free Memory Space
- [GOSUB](#kw-gosub) - Call a BASIC Subroutine
- [GOTO](#kw-goto) - Branch Program Execution
- [HIMEM](#kw-himem) - Get High Memory Address
- [IF](#kw-if) - Test Relational Expression
- [IMP](#kw-imp)
- [INKEY$](#kw-inkey) - Poll Keyboard
- [INP](#kw-inp) - Input From a Port
- [INPUT](#kw-input) - Input Data From Keyboard
- [INSTR](#kw-instr) - Search a String
- [INT](#kw-int) - Get Whole Number Representation
- [IPL](#kw-ipl) - Define Warm Start Program
- [KEY](#kw-key) - Define Function Keys
- [KILL](#kw-kill) - Delete a RAM File
- [LCOPY](#kw-lcopy) - Copy Screen to Printer
- [LEFT$](#kw-left) - Return Left Portion of a String
- [LEN](#kw-len) - Get Size of a String
- [LET](#kw-let) - Assignment Statement
- [LFILES](#kw-lfiles)
- [LINE](#kw-line) - Draw a Line on the Screen
- [LIST](#kw-list) - List Program on the Screen
- [LLIST](#kw-llist) - List Program on the Printer
- [LOAD](#kw-load) - Load a BASIC Program
- [LOC](#kw-loc)
- [LOF](#kw-lof)
- [LOG](#kw-log) - Natural Logarithm
- [LPOS](#kw-lpos) - Printer Column Position
- [LPRINT](#kw-lprint) - Print Data on Printer
- [MAX](#kw-max)
- [MDM](#kw-mdm) - Enable/Disable Modem Interrupt
- [MENU](#kw-menu) - Return to Menu
- [MERGE](#kw-merge) - Merge Two Programs
- [MID$](#kw-mid) - Get Middle Characters of String
- [MOD](#kw-mod) - Modulo (remainder)
- [MOTOR](#kw-motor) - Turn Cassette Motor On and Off
- [NAME](#kw-name) - Rename a RAM file
- [NEW](#kw-new) - Erase the Current Program
- [NEXT](#kw-next) - See FOR...NEXT
- [NOT](#kw-not) - Logical NOT
- [OFF](#kw-off)
- [ON](#kw-on) - Define Communications Interrupt
- [OPEN](#kw-open) - Open a File for I/O
- [OR](#kw-or) - Logical OR
- [OUT](#kw-out) - Output a Byte to a CPU Port
- [PEEK](#kw-peek) - Get a Value From Memory
- [POKE](#kw-poke) - Load a Value into Memory
- [POS](#kw-pos) - Get Screen Position
- [POWER](#kw-power) - Automatic Power Down
- [PRESET](#kw-preset) - Turn Off an LCD Pixel
- [PRINT](#kw-print) - Print Data on the Screen
- [PSET](#kw-pset) - Turn On LCD Pixels
- [READ](#kw-read) - Read Values From a DATA List
- [REM](#kw-rem) - Comment
- [RESTORE](#kw-restore) - Reset the DATA Statement Pointer
- [RESUME](#kw-resume) - Resume Execution After an Error
- [RETURN](#kw-return) - Returns from a subroutine
- [RIGHT$](#kw-right) - Return Right Portion of a String
- [RND](#kw-rnd) - Return Pseudo-Random Number
- [RUN](#kw-run) - Execute a New BASIC Program
- [SAVE](#kw-save) - Save a BASIC Program
- [SCREEN](#kw-screen) - Locks/Unlocks LABEL Line
- [SGN](#kw-sgn) - Algebraic Sign
- [SIN](#kw-sin) - Trigonometric Sine
- [SOUND](#kw-sound) - Output a Tone
- [SPACE$](#kw-space) - String of Spaces
- [SQR](#kw-sqr) - Square Root
- [STEP](#kw-step)
- [STOP](#kw-stop) - Stop Execution
- [STR$](#kw-str) - Convert a Number to a String
- [STRING$](#kw-string) - Define a String of Characters
- [TAB(](#kw-tab)
- [TAN](#kw-tan) - Trigonometric Tangent
- [THEN](#kw-then) - Used with IF to specify true branch
- [TIME$](#kw-time) - Current Time
- [TO](#kw-to)
- [USING](#kw-using)
- [VAL](#kw-val) - Convert Strings To Numbers
- [VARPTR](#kw-varptr) - Get Address of a Variable
- [WIDTH](#kw-width)
- [XOR](#kw-xor) - Logical XOR
- [\](#kw-symbol-126)
- [^](#kw-symbol-127)

<a id="kw-symbol-0"></a>
### '
- Variants: `'`
- Syntax: `'`
- Back: [index](#index)

<a id="kw-symbol-1"></a>
### *
- Variants: `*`
- Syntax: `*`
- Back: [index](#index)

<a id="kw-symbol-2"></a>
### +
- Variants: `+`
- Syntax: `+`
- Back: [index](#index)

<a id="kw-symbol-3"></a>
### -
- Variants: `-`
- Syntax: `-`
- Back: [index](#index)

<a id="kw-symbol-4"></a>
### /
- Variants: `/`
- Syntax: `/`
- Back: [index](#index)

<a id="kw-symbol-5"></a>
### <
- Variants: `<`
- Syntax: `<`
- Back: [index](#index)

<a id="kw-symbol-6"></a>
### =
- Variants: `=`
- Syntax: `=`
- Back: [index](#index)

<a id="kw-symbol-7"></a>
### >
- Variants: `>`
- Syntax: `>`
- Back: [index](#index)

<a id="kw-abs"></a>
### ABS
- Variants: `ABS`
- Syntax: `ABS(numeric expression)`
- Description: Absolute value
- Back: [index](#index)

<a id="kw-and"></a>
### AND
- Variants: `AND`
- Syntax: `expression AND expression`
- Description: Logical AND
- Back: [index](#index)

<a id="kw-asc"></a>
### ASC
- Variants: `ASC`
- Syntax: `ASC(string expression)`
- Description: ASCII code of first character
- Back: [index](#index)

<a id="kw-atn"></a>
### ATN
- Variants: `ATN`
- Syntax: `ATN(numeric expression)`
- Description: Arctangent
- Notes: This function returns the arctangent of numeric expression (in radians). The resulting value ranges from - D to D. Example ARC = ATN(TH) If TH contains the value 0.5, then this statement sets ARC equal to 0.46364760900081.
- Back: [index](#index)

<a id="kw-beep"></a>
### BEEP
- Variants: `BEEP`
- Syntax: `BEEP`
- Description: Emit a Tone
- Notes: This command causes the sound generator to emit a tone for approximately 1/2 second. Example 10 BEEP emits a \"beep.\"
- Back: [index](#index)

<a id="kw-call"></a>
### CALL
- Variants: `CALL`
- Syntax: `CALL address, expression1, expression2`
- Description: Call a Machine Level Subroutine
- Notes: Calls a machine level subroutine beginning at address. Upon entry to the subroutine, the A register contains the value of expressionl and the HL register contains the value of expression2. expressionl is optional and may range from 0 to 255, expression2 is also optional and may range from -32768 to 65535. Example 100 CALL 60000,10,VARPTR(AZ) calls a subroutine beginning at address 60000. Upon entry to the subroutine, register A contains 10, and register HI. contains the address of the variable A%.
- Back: [index](#index)

<a id="kw-cdbl"></a>
### CDBL
- Variants: `CDBL`
- Syntax: `CDBL (numeric expression)`
- Description: Convert to Double-Precision
- Notes: This function converts the value of numeric expression to a double-precision number according to the conversion rules given under \"Data Types and Data Manipulation.\" Example 10 A# = CDBL(AZ) if A% contains 34, then A# contains 34.000000000000.
- Back: [index](#index)

<a id="kw-chr"></a>
### CHR$
- Variants: `CHR$`
- Syntax: `CHR$(numeric expression)`
- Description: Character Value
- Notes: The CHR$ function returns the ASCII character for the value of numeric expression. numeric expression must lie in the range of 0 to 255. CHR$ is the inverse of the function ASC. For a list of ASCII codes, see the Appendices. Examples PRINT CHR$(65) prints the character A. PRINT \"He said \"CHR$(34);\"Hello\";CHR$(34) prints the message He said \"Hello\" (Note: 34 is the ASCII code for the double quote mark, \".\")
- Back: [index](#index)

<a id="kw-cint"></a>
### CINT
- Variants: `CINT`
- Syntax: `CINT(numeric expression)`
- Description: Convert to Integer
- Notes: CINT truncates the decimal portion of numeric expression. The resulting valuc must lie in the range -32768 to 32767. Examples 10 A% = CINT(45.67) sets A% equal to 45. 10 A% = CINT(-2343.55823) sets A% equal to -2343.
- Back: [index](#index)

<a id="kw-clear"></a>
### CLEAR
- Variants: `CLEAR`
- Syntax: `CLEAR string space, high memory`
- Description: Clear Variables and Allocate String Space
- Notes: This command clears the values in all numeric and string variables, and closes all open files. string space is a numeric expression and is optional. If present, BASIC allocates the specified number of bytes of memory for string storage. If you omit string space, BASIC allocates 256 bytes by default. high memory is a numeric expression and is also optional. If present, BASIC sets the top of its memory at the given value. You may use the word MAXRAM to specify the maximum value available RAM (dependent on the configuration of your Model 100). If high memory isn't used, then BASIC defaults to MAXRAM. If you intend on using machine-language subroutines, you need to use CLEAR to protect high memory space for the subroutines. Note that when you enter BASIC, it always resets the string space allocation to 256 bytes. However, if you have protected a portion of high memory in a previous program, BASIC keeps this part of memory protected until you CLEAR it. Examples 10 CLEAR clears all variables, closes open files, sets the available string space to 256 bytes, and releases all of available memory to BASIC: CLEAR 100,50000 clears all variables, closes open files, sets the available string space to 100 bytes, and set 50000 as the highest memory address available to BASIC.
- Back: [index](#index)

<a id="kw-cload"></a>
### CLOAD
- Variants: `CLOAD`
- Syntax: `a CLOAD \"filename\", R`
- Description: Load a Program From Cassette
- Notes: The CLOAD command clears the current BASIC program and loads a BASIC program from cassette tape. filename consists of a string of one to six characters, the first of which is a letter. filename is optional; if used, BASIC searches the tape until it finds filename. If not used, BASIC loads the first BASIC program it finds. R is also optional; if used, BASIC executes the new program as soon as the load is complete. As BASIC searches the tape, it prints out the names of any files it skips over. (Note: CLOAD is identical to LOAD \"CAS:) Examples `CLOAD \"ACCT\",R` loads and runs the BASIC program ACCT stored on cassette tape. `CLOAD` loads the first BASIC program found on the cassette tape.
- Back: [index](#index)

<a id="kw-close"></a>
### CLOSE
- Variants: `CLOSE`
- Syntax: `CLOSE file number list`
- Description: Close Open Files
- Notes: This command closes the files specified in file number list. file number is the number under which the file was opened (See OPEN), and is optional; if omitted, BASIC closes all open files. Example CLOSE 1,2,3 closes the files associated with file numbers 1, 2, and 3.
- Back: [index](#index)

<a id="kw-cls"></a>
### CLS
- Variants: `CLS`
- Syntax: `CLS`
- Description: Clear Screen
- Notes: CLS turns off all of the LCD pixels on the Screen and moves the Cursor to the upper-left corner of the Screen. Example 100 CLS: PRINT \"The old screen is gone!\" This clears the Screen and prints out the message in the upper-left corner.
- Back: [index](#index)

<a id="kw-com"></a>
### COM
- Variants: `COM ON/OFF/STOP`
- Syntax: `COM ON or OFF or STOP`
- Description: Enable/Disable Communications Interrupt
- Notes: This enables or disables the ON COM interrupt. ON enables the interrupt so that if a character is received via the RS-232C port, BASIC jumps to the subroutine defined in the ON COM command OFF disables the interrupt. STOP disables the interrupt. However, BASIC \"remembers\" that a character was received, so that if you issue a COM ON command, BASIC jumps immediately to the interrupt subroutine. Examples 10 COM ON enables the communications interrupt.
- Back: [index](#index)

<a id="kw-cont"></a>
### CONT
- Variants: `CONT`
- Syntax: `CONT`
- Description: Continue Execution
- Notes: CONT resumes execution of a program after you have pressed (BREAK) or after BASIC has encountered a STOP command in the program. This command is primarily for debugging purposes. After you press (BREAK) or BASIC encounters a STOP command, you can examine any of the variables with the PRINT command, as well as change variable values. To continue, simply type CONT and press (ENTER). (Note: You cannot resume execution if you change any of the lines of the program, either through editing, deletion, or insertion. Example CONT resumes execution of the BASIC program.
- Back: [index](#index)

<a id="kw-cos"></a>
### COS
- Variants: `COS`
- Syntax: `COS(numeric expression)`
- Description: Cosine
- Notes: This function returns the cosine of angle given by numeric expression. You must give this angle in radians. Example 10 Y = COS(60*0.01745329) assigns Y the value 0.50000013093981.
- Back: [index](#index)

<a id="kw-csave"></a>
### CSAVE
- Variants: `CSAVE`
- Syntax: `CSAVE \"filename\", A`
- Description: Save a Program on Cassette
- Notes: CSAVE stores the current BASIC program on cassette tape. filename consists of a string of one to six characters, the first of which is a letter. A is optional; if used, BASIC saves the program in ASCII format. If omitted, BASIC stores the program in a compressed form. To perform certain commands, such as MERGE, programs must be stored in ASCII format. However, for most uses, you'll want your programs stored in a compressed format to save space on the tape. (Note: This command functions identically to SAVE \"CAS:\") CSAVE \"TANDY\" This example saves the current program onto cassette tape (in compressed format) under the name \"TANDY.\" CSAVE \"TANDY\", A This line saves the current program onto cassette tape (in ASCII format) under the name \"TANDY.\"
- Back: [index](#index)

<a id="kw-csng"></a>
### CSNG
- Variants: `CSNG`
- Syntax: `CSNG(numeric expression)`
- Description: Convert to Single Precision
- Notes: CSNG returns the single-precision form of numeric expression, according to the conversion rules listed under \"Data Conversion.\" Example 10 A! = CSNG(0.66666666666) sets A! equal to 0.666667.
- Back: [index](#index)

<a id="kw-csrlin"></a>
### CSRLIN
- Variants: `CSRLIN`
- Syntax: `CSRLIN`
- Description: Vertical Cursor Position
- Notes: This function returns the vertical position (line number) of the Cursor, where 0 is the top line and 7 is the bottom line. Example 10 CLS: AZ = CSRLIN clears the Screen and assigns A% the value 0.
- Back: [index](#index)

<a id="kw-data"></a>
### DATA
- Variants: `DATA`
- Syntax: `DATA constant list`
- Description: Define a Data Set
- Notes: DATA defines a set of constants (numeric and/or string) to be accessed by a READ command elsewhere in the program. See also READ and RESTORE. Example DATA 10,25.50,15,\"Probabilities\",\"Total\" stores the given values.
- Back: [index](#index)

<a id="kw-date"></a>
### DATE$
- Variants: `DATE$`
- Syntax: `DATE$`
- Description: Current Date
- Notes: DATE$ keeps track of the current date, in string form. You may access it like any string variable, including setting a new date. Date string has the form MM/DD/YY where 01<MMa13, 01<DDa39, and 00aYYa99. BASIC automatically updates DATE$ when the clock changes from 23:59:59 to 00:00:00. Examples PRINT DATE$ prints the current date. DATE$ = \"11/02/82\" sets the current date to November 11, 1982.
- Back: [index](#index)

<a id="kw-day"></a>
### DAY$
- Variants: `DAY$`
- Syntax: `DAY$`
- Description: Current Day of Week
- Notes: This string variable keeps track of the current day of the week, in string form. You may access DAY$ like any string variable, including setting a new day. DAY$ consists of a three letter string made up of the first three letters of the day name (for example, Thu signifies Thursday). BASIC automatically updates DAY$ when the clock changes from 23:59:59 to 00:00:00. Examples PRINT DAY$ prints the current day of the week. DAY$ = \"Fri sets the current day as Friday. (Note that BASIC doesn't care whether the DAY$ string is in upper- or lowercase a it automatically converts the string to one uppercase letter followed by two lowercase letters.) Valid strings include: Mon Tue Wed Thu Fri Sat Sun and all upper- and lowercase combinations of each.
- Back: [index](#index)

<a id="kw-def"></a>
### DEF
- Variants: `DEF`
- Syntax: `DEF`
- Back: [index](#index)

<a id="kw-dim"></a>
### DIM
- Variants: `DIM`
- Syntax: `DIM variable name(dimensions) list`
- Description: Define Array Size
- Notes: DIM defines variable name as an array with the given dimensions, dimensions is a list of one or more numeric expressions, defining the \"height,\" \"width,\" and so on for the array. The expressions must evaluate to positive values. Since BASIC arrays begin with the \"zeroth\" clement, the actual size in any dimension is one plus the given dimension. The number of dimensions you may list depends only on the amount of available memory. To redimension an array, you must first use the command CLEAR (this destroys all variable values). Examples DIM A$(10), BALZ(10,10) defines a string array, A$, which consists of 11 elements, A$(0) through A$(10), and an integer array, BAL%, which consists of 121 elements, BAL%(0,0) through BAL%(10,10).
- Back: [index](#index)

<a id="kw-dski"></a>
### DSKI$
- Variants: `DSKI$`
- Syntax: `DSKI$`
- Back: [index](#index)

<a id="kw-dsko"></a>
### DSKO$
- Variants: `DSKO$`
- Syntax: `DSKO$`
- Back: [index](#index)

<a id="kw-edit"></a>
### EDIT
- Variants: `EDIT`
- Syntax: `EDIT line number range`
- Description: Edit a BASIC Program
- Notes: EDIT enters the text editor using the lines given by line number range, line number range may be: null edit the entire program. line1-line2 edit from line1 to line2, inclusive. -line2 edit from beginning of the program to line2. line1- edit from line1 to the end of the program. edit last accessed line number (last edited, entered, listed, and so on). To exit Edit, press F8. Note that while in the Edit Mode, you may insert and delete lines. However, if you insert a line which already exists in the program, the new line replaces the old line. If you edit a line in such a way that it is not a valid program line (for example, longer than 255 characters, no line number, invalid line number), the Editor tells you Text Ill-formed Press Space bar for TEXT Pressing the space bar returns you to the Text Editor. For more information on the Text Editor, see Part II of this manual. Examples EDIT lets you edit the entire program. EDIT 100-500 lets you edit lines 100 through 500. EDIT 100- lets you edit from line 100 to the end of the program.
- Back: [index](#index)

<a id="kw-else"></a>
### ELSE
- Variants: `ELSE`
- Syntax: `IF condition THEN commands ELSE commands`
- Description: Used with IF to specify false branch
- Back: [index](#index)

<a id="kw-end"></a>
### END
- Variants: `END`
- Syntax: `END`
- Description: End Execution
- Notes: END terminates execution of the BASIC program. END statements may be placed anywhere in the program. If omitted, BASIC executes up to the physical end of the program. Example 10 INPUT S1, S2 20 GDSUB 100 . . . 90 END 100 H=SQR(S1*S1+S2*S2) 110 RETURN The END statement in line 90 prevents BASIC from entering the subroutine in line 100 from anywhere but a GOSUB call.
- Back: [index](#index)

<a id="kw-eof"></a>
### EOF
- Variants: `EOF`
- Syntax: `EOF (file number)`
- Description: Test for End-of-File
- Notes: EOF tests for an end-of-file condition on RAM, cassette, or communications files. file number is the buffer number assigned when the file was OPEN'ed. The function returns a \"logical\" answer, either \"true\" (-1) if you have reached the end of the file, or else \"false\" (0) if you have not reached the end of the file. Example 100 IF EOF(1) THEN 200 checks the file assigned to buffer 1 for end of file If true, then the program jumps to line 200.
- Back: [index](#index)

<a id="kw-eqv"></a>
### EQV
- Variants: `EQV`
- Syntax: `EQV`
- Back: [index](#index)

<a id="kw-erl"></a>
### ERL
- Variants: `ERL`
- Syntax: `ERL`
- Description: Get Line Number of Error
- Notes: ERL returns the line number of the last error. If the last error which occured was not in a program line but trom a direct mode command, ERL returns the value 65535. This command is useful in conjunction with the ON ERROR GOTO command. Example 100 ON ERROR GOTO 2000 . . . 2000 IF ERR = 23 THEN RESUME ELSE PRINT \"Error\";ERR; \"in line\";ERL: STOP If an error occurs in the program, execution jumps to line 2000. If the error was an I/O error (ERR = 23), then BASIC simply retries the I/O (RESUME). If there was some other type of error, say a syntax error in line 1000, then BASIC displays the message: Error 2 in line 1000 and stops the program. See also ON ERROR and ERR.
- Back: [index](#index)

<a id="kw-err"></a>
### ERR
- Variants: `ERR`
- Syntax: `ERR`
- Description: Get Error Code Number
- Notes: This function returns the error code number of the last error. This command is useful in conjunction with the ON ERROR GOTO command. Example 100 ON ERROR GOTO 2000 2000 IF ERR = 18 THEN PRINT \"I/O Error \" ELSE STOP 2010 INPUT \"Continue(Y/N)\"; A$ 2020 IF A$ = \"Y\" THEN RESUME ELSE STOP If an error occurs in the program, then BASIC jumps to line 2000. If the error was an I/O error (error 18), then BASIC prints out the message and prompt and waits on your response
- Back: [index](#index)

<a id="kw-error"></a>
### ERROR
- Variants: `ERROR`
- Syntax: `ERROR numeric expression`
- Description: Simulate an Error
- Notes: This command simulates the error specified by numeric expression. BASIC behaves just as if your program had committed the error. Example ERROR 4 prints OD Error. 100 ERROR 10 prints DD Error in 100 and stops execution of the program.
- Back: [index](#index)

<a id="kw-exp"></a>
### EXP
- Variants: `EXP`
- Syntax: `EXP (numeric expression)`
- Description: Exponential (Antilog)
- Notes: EXP returns the exponential (or \"natural\" antilog) of numeric expression. numeric expression must be in the range  87.3365 or an overflow error occurs. EXP is the opposite of the function LOG. Example PRINT EXP(14) prints 1202604.2841644, the natural antilog of 14.
- Back: [index](#index)

<a id="kw-files"></a>
### FILES
- Variants: `FILES`
- Syntax: `FILES`
- Description: Display File Names
- Notes: This command will cause BASIC to display all of the files currently stored in RAM without exiting BASIC. Example FILES
- Back: [index](#index)

<a id="kw-fix"></a>
### FIX
- Variants: `FIX`
- Syntax: `FIX (numeric expression)`
- Description: Truncate Real Numbers
- Notes: FIX returns the whole number portion of numeric expression. (Note: The difference between FIX and INT is that for negative numbers, FIX simply truncates numeric expression while INT returns the whole number not greater than numeric expression. Examples 10 A = FIX(1440.43) sets A equal to 1440. 10 A = FIX(-33494123.4442) sets A equal to -33494123.
- Back: [index](#index)

<a id="kw-for"></a>
### FOR
- Variants: `FOR...NEXT`
- Syntax: `FOR counter variable = initial value TO final value STEP increment ... NEXT counter variable`
- Description: Establish Program Looping
- Notes: These commands execute the statements between the FOR and NEXT loop repetitively, varying counter variable from initial value to final value, adding increment to it each time BASIC ends the loop. initial value, final value, and increment are all numeric expressions. STEP increment is optional; if omitted, BASIC assumes STEP 1. BASIC executes the loop at least once, even if variable exceeds final value the first time the FOR statement is read. Also, BASIC evaluates initial value, final value, and increment the first time it executes the line. If these expressions are variables, changing the values of these variables later in the loop has no effect on the execution of the loop. You may \"nest\" FOR...NEXT loops with other FOR...NEXT loops. The number of nested loops is dependent only on the size of remaining memory. Note that all inner loops must be contained entirely within the next outer loop. For example: 10 FOR I=1 TO 100 20 FOR J=1 TO 20 30 B(I,J) = A(I,J) 40 NEXT J 50 NEXT I Legal 10 FOR I=1 TO 100 20 FOR J=1 TO 20 30 B(I,J) = A(I,J) 40 NEXT I 50 NEXT J Illegal Examples 10 FOR I=10 TO 1 STEP -1 20 PRINT I; 30 NEXT prints the numbers 10 through 1. (Note that you may use negative values for increment.) 10 FOR K=B TO E 20 PRINT K 30 NEXT If B equals 4 and E equals 2, this routine prints out the number 4. Since no STEP is specified, STEP 1 is assumed. BASIC then increments K by 1 to the value 5. Since 5 is greater than 2, the loop ends. 10 FOR I=1 TO 3 20 PRINT \"OUTER LOOP\" 30 FOR J=1 TO 2 40 PRINT \"          INNER LOOP\" 50 NEXT J 60 NEXT I prints: OUTER LOOP INNER LOOP INNER LOOP OUTER LOOP INNER LOOP INNER LOOP OUTER LOOP INNER LOOP INNER LOOP Note that lincs 50 and 60 could be condensed to NEXT J,I (but not NEXT I,J). You may also simply say NEXT and BASIC will \"know\" which loop it is in.
- Back: [index](#index)

<a id="kw-fre"></a>
### FRE
- Variants: `FRE`
- Syntax: `FRE(dummy expression)`
- Description: Free Memory Space
- Notes: FRE returns the current amount of unused numeric memory in bytes when dummy expression is numeric and the current total amount of unused string space when dummy expression is string type. Examples PRINT FRE(0) prints out the current free numeric memory space. ?FRE (\" \") prints out the current free string space.
- Back: [index](#index)

<a id="kw-gosub"></a>
### GOSUB
- Variants: `GOSUB`
- Syntax: `GOSUB line number`
- Description: Call a BASIC Subroutine
- Notes: This command transfers program control to the subroutine beginning at line number. When BASIC encounters a RETURN command in the subroutine, it jumps back to the command immediately following the GOSUB. You must always terminate a subroutine with a RETURN command. Example 100 GOSUB 1000 110 PRINT \"Average = \"; AV . . . 990 END 1000 'Averaging Subroutine 1010 FOR I=1 TO 20 1020 SM = A(I) 1030 NEXT I 1040 AV = SM / 20 1050 RETURN Line 100 calls the subroutine at line 1000. BASIC executes lines 1000 through 1040, and then jumps back to line 110 and begins execution there.
- Back: [index](#index)

<a id="kw-goto"></a>
### GOTO
- Variants: `GOTO`
- Syntax: `GOTO line number`
- Description: Branch Program Execution
- Notes: GOTO branches program control to the specified line number. Used alone, GOTO line number results in an \"unconditional\" (or automatic) branch. You may also use GOTO in conjunction with conditional expressions, such as IF and ON ERROR. This results in \"conditional\" branching. You can use GOTO in the Immediate Mode to cause execution to begin at the specified line number, without an automatic CLEAR. This allows you to enter a program at a specific point, without destroying any old variables (the command RUN tells BASIC to first clear all of memory before beginning execution). Examples 200 GOTO 10 branches control unconditional to line 10. 100 IF AN$ = \"Y\" GOTO 1000 ELSE GOTO 2000 if ANS equals \"Y,\" then BASIC branches to line 1000; otherwise BASIC branches to line 2000. A=1.32 : GOTO 1000 assigns A the value 1.32 and begins execution at line 1000.
- Back: [index](#index)

<a id="kw-himem"></a>
### HIMEM
- Variants: `HIMEM`
- Syntax: `HIMEM`
- Description: Get High Memory Address
- Notes: This function returns the top address of memory available to BASIC. You may change this value with the CLEAR command. Example PRINT HIMEM prints the current top address of BASIC memory.
- Back: [index](#index)

<a id="kw-if"></a>
### IF
- Variants: `IF...THEN...ELSE`
- Syntax: `IF relational or logical expression THEN command(s)1 ELSE command(s)2`
- Description: Test Relational Expression
- Notes: The IF/THEN statements test the logical \"truth\" of relational or logical expression (relational and logical expressions are defined under \"Expressions,\" earlier in this section). If the expression is \"true,\" then BASIC executes command(s)1. If the expression is \"false,\" BASIC cxecutes command(s)2. If THEN command(s)/ is a THEN GOTO line number, BASIC also accepts THEN line number and GOTO line number as equivalent terms. ELSE command(s)2 is optional; if omitted, BASIC assumes the ELSE clause is the next line. If ELSE command(s)2 is a GOTO line number, then ELSE line number is an equivalent term. In numeric terms, \"false\" has the value zero, and \"true\" is any value except zero. Example 10 IF A < 100 THEN 100 20 tests the condition A < 100 a if true, then BASIC jumps to line 100; if false, then BASIC continues execution at line 20. 10 IF A = 10 OR A = 20 THEN B$ = \"Paid\" ELSE B$ = \"Not Paid\" tests the condition A = 10 OR A = 20 --- if true, then BASIC assigns B$ the string \"Paid\"; if false, then BASIC assigns B$ the string \"Not Paid\".
- Back: [index](#index)

<a id="kw-imp"></a>
### IMP
- Variants: `IMP`
- Syntax: `IMP`
- Back: [index](#index)

<a id="kw-inkey"></a>
### INKEY$
- Variants: `INKEY$`
- Syntax: `INKEY$`
- Description: Poll Keyboard
- Notes: This function returns the string value of the key currently pressed, if any. If no key is pressed, the function returns a null character (\"\"). In either case, BASIC doesn't wait for keyboard input, but goes to the next statement. (Note: If you press an undefined Function Key, PASTE or LABEL, INKEY$ returns an ASCII 0 with a length of 1.) Example 10 A$ = INKEY$ 20 IF A$ = \"\" THEN 10 30 . . . sets A$ equal to the string value of any key pressed. If you haven't pressed a key, then A$ contains the null character (\" \") and BASIC jumps back to line 10. If you have pressed a key, A$ contains the character representation of the key you pressed, and hence BASIC continues execution at line 30
- Back: [index](#index)

<a id="kw-inp"></a>
### INP
- Variants: `INP`
- Syntax: `INP (port number)`
- Description: Input From a Port
- Notes: INP returns a byte from the specified port. port number must be a numeric expression in the range of 0 to 255. INP is the complement function to the OUT command. Example A% = INP(5) sets A% equal to the byte value at port 5.
- Back: [index](#index)

<a id="kw-input"></a>
### INPUT
- Variants: `INPUT`, `INPUT #`
- Syntax: `INPUT \"prompt\";variable list`; `INPUT # file number, variable list`
- Description: Input Data From Keyboard Input From a File
- Notes: INPUT stops execution of your program until you enter data from the keyboard. The values you enter must be constants and must correspond in both number and type to the variables in variable list. variable list consists of any number of variable names, both string and numeric, separated by commas. The optional \"prompt\" is any valid string expression. BASIC displays prompt prior to accepting your input. While BASIC is awaiting your input, it displays a question mark. At this point, you may enter enough data, separated by commas, for all of the variables in variable list, terminated with ENTER. Alternatively, you may enter each data item separately, pressing (ENTER) after each. In the latter case, after accepting the first value, BASIC displays two question marks as a prompt for subsequent input. For string input, you may enclose the data in quotes, although BASIC doesn't require this. However, if the input string contains any leading blanks, commas, or colons, you must use quote marks. BASIC lets you input numeric data into string variables. (BASIC stores the ASCII value --- not the numeric value!) For numeric input, BASIC performs any necessary conversion to the numbers so that they fit into the variable. This conversion is identical to other data conversions in the program. If you attempt to input string data into a numeric variable, BASIC displays the message ?Redo from start followed by another?, and lets you try again. See \"Data Conversion,\" earlier in this section for the data conversion rules. Examples 10 INPUT \"X and Y Coordinates\";X,Y BASIC displays: X and Y Coordinates? If you type 10,20 and press ENTER, then BASIC assigns X the value 20 and Y the value 30. If you type 10 and press (ENTER), then BASIC assigns X the value 20, and then displays: ?? You may then type in the value for Y and press (ENTER). 100 INPUT A$, B%, C$, D This statement calls for you to input a string, a number, a string, and finally another number. BASIC prompts you with a ?. You may then type in: Fort Worth, 5641.321, Texas, 76109 [ENTER] This assigns \"Fort Worth\" to AS, 5641 to B% (note the conversion), \"Texas\" to CS, and 76109 to D. The following is equivalent: \"Fort Worth\" (ENTER) 5641 (ENTER) Texas (ENTER) 76109 (ENTER)
- Notes: This command inputs data sequentially from the file opened under file number. You may input data with this command from RAM, cassette tape, the RS-232C port, or the modem. INPUT # functions identically to INPUT from the keyboard, except that the data comes from a file, and BASIC displays no question mark prompt. The data in the file must be separated by commas. See also OPEN. Example 10 INPUT #1,A$,B$,C inputs values for A$, B$ and C from the file opened as file #1.
- Back: [index](#index)

<a id="kw-instr"></a>
### INSTR
- Variants: `INSTR`
- Syntax: `INSTR (start position,search string,match string)`
- Description: Search a String
- Notes: INSTR searches search string for the first occurrence of match string, beginning at start position. If the string is found, INSTR returns the position in the string where it occurs. If string isn't found, then INSTR returns a zero. start position is optional; if omitted INSTR starts the search at position one. Also, if start position is greater than the length of search string, INSTR returns a zero. Example PRINT INSTR(\"dimethylsulfate\", \"sulfate\") prints 9 on the Screen (\"sulfate\" begins at position 9 of \"dimethylsulfate\") AX = INSTR(5,NM$,\"Jim\") If NMS contains the string \"JimBob\", then this line sets A% equal to 0 (\"Jim\" does not occur past position 5 of \"JimBob\").
- Back: [index](#index)

<a id="kw-int"></a>
### INT
- Variants: `INT`
- Syntax: `INT(numeric expression)`
- Description: Get Whole Number Representation
- Notes: INT returns the whole number representation of numeric expression, not greater than numeric expression. (Note: The difference between the functions INT and FIX is that for negative numbers, FIX simply truncates numeric expression while INT returns the whole number not greater than numeric expression.) Examples A# = INT(21444331113.443) sets A# equal to 21444331113. A# = INT(-214.995) sets A# equal to -215.
- Back: [index](#index)

<a id="kw-ipl"></a>
### IPL
- Variants: `IPL`
- Syntax: `IPL \"filename\"`
- Description: Define Warm Start Program
- Notes: IPL defines filename as the warm-startup program. filename is the name of a current RAM file. After executing this command, this program runs whenever you turn on your Model 100. Example IPL \"TIMSET.BA\" Now whenever you turn on the Computer, it will execute the program TIMSET.BA. IPL will execute properly only if the Computer is turned off while in BASIC with the proper IPL program loaded.
- Back: [index](#index)

<a id="kw-key"></a>
### KEY
- Variants: `KEY`, `KEY LIST`, `KEY ON/OFF/STOP`
- Syntax: `KEY function key number,string expression`; `KEY LIST`; `KEY (function key number) ON/OFF/STOP`
- Description: Define Function Keys List Function Key Definitions Enable/Disable Function Key Interrupts
- Notes: KEY defines function key number as string expression. function key number is a numeric expression from 1 to 8 and string expression must be 15 or less characters. Example KEY 6,\"TIME$\" + CHR$(13) defines Function Key 6 as ?TIMES followed by a carriage return. Now whenever you press Function Key 6, BASIC returns the time. (Remember that \"?\" is an abbreviation for PRINT. and that ASCII character 13 is the code generated when you press ENTER.) To reset the function keys to the cold start default, you must \"call\" two subroutines with the following commands: CALL 23164,23366 CALL 27795 This resets the function keys to their original value.
- Notes: Lists on the Screen the current definitions for the Function Keys, in the format: key 1 key 2 key 3 key 4 key 5 key 6 key 7 key 8 Example KEY LIST Unless you have altered the function key definitions, BASIC displays: Files Load \" Save Run List Menu
- Notes: This statement enables or disables the function key interrupt. ON enables the interrupt so that if you press a Function Key, BASIC branches to the ON KEY subroutine. OFF disables the interrupt. STOP disables the interrupt, however, BASIC \"remembers\" that you pressed a Function Key, so that if you issue a KEY ON command, BASIC jumps immediately to the interrupt subroutine. See ON KEY GOSUB. Examples 100 KEY (2) ON enables Function Key 2. 100 KEY ON enables all Function Keys. 100 KEY (4) OFF disables Function Key 4.
- Back: [index](#index)

<a id="kw-kill"></a>
### KILL
- Variants: `KILL`
- Syntax: `KILL \"filename\"`
- Description: Delete a RAM File
- Notes: KILL deletes a RAM file. filename is a string of one to six characters, the first of which must be a letter. plus a two character extension. You must include the file's extension. If you have 200 bytes or less of free memory, KILL may not delete a file. If this situation occurs, delete program lines \"manually\" or go to TEXT, \"select\" a file, and put it in the PASTE Buffer. Then return to BASIC and KILL the unwanted files. Example KILL \"BILLS.BA\" deletes the RAM file BILLS.BA.
- Back: [index](#index)

<a id="kw-lcopy"></a>
### LCOPY
- Variants: `LCOPY`
- Syntax: `LCOPY`
- Description: Copy Screen to Printer
- Notes: Prints the text on the Screen onto the printer. LCOPY ignores non-text data. Example LCOPY prints the text on the Screen onto the printer.
- Back: [index](#index)

<a id="kw-left"></a>
### LEFT$
- Variants: `LEFT$`
- Syntax: `LEFT$(string expression, length)`
- Description: Return Left Portion of a String
- Notes: LEFT returns the first length characters of string expression. length is a numeric expression. Example 10 AC$ = LEFT$(PN$,3) If PNS contains the string \"81755552161,\" then after execution of this command ACS contains the string \"817\".
- Back: [index](#index)

<a id="kw-len"></a>
### LEN
- Variants: `LEN`
- Syntax: `LEN(string expression)`
- Description: Get Size of a String
- Notes: LEN returns the number of characters in string expression. Example 100 INPUT NM$ 110 IF LEN(NM$) < 20 THEN NM$ = NM$ + \" \": GOTO 110 adds spaces to the end of NM$ so that it is at least 20 characters long. This \"left justifies\" the input string, while \"padding\" on the right with spaces.
- Back: [index](#index)

<a id="kw-let"></a>
### LET
- Variants: `LET`
- Syntax: `LET variable = expression`
- Description: Assignment Statement
- Notes: This statement assigns value of expression to variable, variable must be of the same data type as expression (that is, numeric or string). For numeric expressions, BASIC performs any conversion necessary to fit expression into variable (see \"Data Conversion,\" for the conversion rules). LET is optional --- it is included in Model 100 BASIC to be compatible with older forms of BASIC. LET A$ = \"The\" and A$ = \"The\" both assign the string \"The\" to A$.
- Back: [index](#index)

<a id="kw-lfiles"></a>
### LFILES
- Variants: `LFILES`
- Syntax: `LFILES`
- Back: [index](#index)

<a id="kw-line"></a>
### LINE
- Variants: `LINE`, `LINE INPUT`
- Syntax: `LINE (x1,y1) - (x2,y2), switch, BF`; `LINE INPUT \"prompt\", string variable`
- Description: Draw a Line on the Screen Input a String from the Keyboard
- Notes: LINE draws a line from coordinates x1,y1 to x2,y2. x1 and x2 are numeric expressions which range from 0 to 239, and y1 and y2 are numeric expressions which range from 0 to 63. (x1,y1) is optional; if not used, BASIC starts the line from the x,y coordinates of the last LINE command, or from 0,0 if this is the first LINE command. You must always include the hyphen. switch is a numeric expression and is optional, if used, odd values of switch tell BASIC to set the points of the line, and even values of switch tell BASIC to reset (that is, erase) the points on the line. If not present, BASIC assumes you mean to set the points of the line. B tells BASIC to draw a box with corners at (x1,y1) and (x2,y2). BF tells BASIC to fill in the box with switch. Both B and BF require that you specify switch. Examples 10 LINE (20,20)-(50,63) 20 LINE - (30,30) draws lines from (20,20) to (50,63), and from (50,63) to (30,30). 10 LINE (20,20)-(50,63),0 erases (resets) all points on a line from (20,20) to (50,63) 10 LINE (0,0)-(239,63),1,B draws a box with corners at (0,0) and (239,63). 10 LINE (0,0)-(239,63),1,BF draws a box with corners at (0,0) and (239,63) and then sets all of the points inside the box.
- Notes: This statement stops execution of your program until you enter a string from the keyboard, then assigns that string to string variable. The optional \"prompt\" is any valid string constant which BASIC displays prior to accepting your input. LINE INPUT differs from INPUT in that: * BASIC doesn't display a question mark prompt * You may have only one variable name * BASIC assigns all input (including commas, leading blanks, and quote marks) to string variable Example 10 LINE INPUT \"Enter Name and Address:\"!NA$ displays: Enter Name and Address: and waits for you to enter data. If you typed: John \"Rocky\" Smith, 5641 Lancaster, East Pearoe, Ohio ENTER BASIC assigns NA$ the string John \"Rocky\" Smith, 5641 E. Lancaster, East Pearoe, Ohio.
- Back: [index](#index)

<a id="kw-list"></a>
### LIST
- Variants: `LIST`
- Syntax: `LIST line number range`
- Description: List Program on the Screen
- Notes: This command lists the line number range of the current program on the Screen, line number range may be: null lists the entire program. line1-line2 lists from linel to line2, inclusive. -line2 list from beginning of the program to line 2. line1- list from linel to the end of the program. lists the last accessed line number (last edited, entered, listed, and so on) Example LIST displays the entire program. LIST 100-300 displays from line 100 to line 300 LIST .- displays from the current line to the end of the program.
- Back: [index](#index)

<a id="kw-llist"></a>
### LLIST
- Variants: `LLIST`
- Syntax: `| LLIST line number range`
- Description: List Program on the Printer
- Notes: LLIST lists the line number range of the current program onto the printer. line number range may be: null lists the entire program. linel-line2 lists from linel to line2, inclusive. -line2 list from beginning of the program to line2. linel- list from linel to the end of the program. lists last accessed line number (last edited, entered, listed, and so on) Example `LLIST` prints out the entire program. `LLIST 100-300` prints out line 100 to line 300. `LLIST .-` prints out from the first line of the program to the current line.
- Back: [index](#index)

<a id="kw-load"></a>
### LOAD
- Variants: `LOAD`
- Syntax: `LOAD \"device:filename or configuration\", R`
- Description: Load a BASIC Program
- Notes: LOAD loads a BASIC program from device. filename consists of a string of one to six characters, the first of which is a letter. device may be RAM, CAS, COM, or MDM. If device is RAM, then you may include the optional extension .BA or .DO. If device is CAS, then you use no extension. For COM, configuration consists of a five character string of the pattern rwpbs, where r Baud Rate This is a number from 1 to 9, where 1=75; 2=110; 3=300; 4=600; 5=1200; 6=2400; 7=4800; 8=9600; 9=19200. w Word Length This is a number from 6 to 8, where 6=6 bits; 7=7 bits; 8=8 bits. p Parity Either E,O,I, or N, where E=Even; O=Odd, I=Ignore; N = None. b Stop Bits Either 1 or 2, where 1=1 stop bit; 2=2 stop bits. s XON/XOFF Status Either E or D, where E = Enable; D = Disable. For MDM, configuration consists of a four character string of the pattern wpbs, defined above. (BASIC automatically sets the baud rate to 300 baud.) R is optional; if used, BASIC runs the incoming program as soon as it has been read in. Note that for MDM and COM, the person on the other end of the communications line must be ready to send the program using the same configurations, after you enter the LOAD command. Cassette loads have several features not found in other load forms: * You may omit filespec, in which case BASIC loads the BASIC program it finds. * If filespec isn't the first program on the tape, BASIC prints the message Skip: followed by the name of the file it is skipping over. * The command CLOAD \"filespec\" functions identically to LOAD \"CAS:filespec\".) See also SAVE. Examples LOAD \"RAM:TIMSET\" loads the BASIC program TIMSET.BA from memory. LOAD \"CAS:ACCT\",R loads and runs the BASIC program ACCT from cassette tape. (Note: The program could have been SAVE'd in either ASCII or binary format.) LOAD \"COM:78N1E\" loads a BASIC program from the RS-232C Communications Line, using 4800 baud, eight bit words, no parity, one stop bit, and line enable. LOAD \"MDM:702E\",R loads a BASIC program from the modem, using seven bit words, odd parity, two stop bits, and line enable.
- Back: [index](#index)

<a id="kw-loc"></a>
### LOC
- Variants: `LOC`
- Syntax: `LOC`
- Back: [index](#index)

<a id="kw-lof"></a>
### LOF
- Variants: `LOF`
- Syntax: `LOF`
- Back: [index](#index)

<a id="kw-log"></a>
### LOG
- Variants: `LOG`
- Syntax: `LOG (numeric expression)`
- Description: Natural Logarithm
- Notes: LOG returns the natural logarithm (base \"e\") of numeric expression. numeric expression must be greater than zero. Example 10 A = LOG(10) sets A equal to 2.302585092994.
- Back: [index](#index)

<a id="kw-lpos"></a>
### LPOS
- Variants: `LPOS`
- Syntax: `LPOS (dummy numeric expression)`
- Description: Printer Column Position
- Notes: This command returns the current position of the printer print head within the printer buffer. Example LPRINT \"Printer head position:\"ILPOS(0) prints the message followed by the number.
- Back: [index](#index)

<a id="kw-lprint"></a>
### LPRINT
- Variants: `LPRINT`, `LPRINT USING`
- Syntax: `LPRINT expression list`; `LPRINT USING \"format string\"; expression list`
- Description: Print Data on Printer Print Formatted Data on Printer
- Notes: LPRINT prints out the values of expression list on the printer. If the expressions are separated by commas, then the printer prints a value and advances to the next \"print zone\" before printing the next value. The print zones are defined every 14 columns (at column 0, column 14, column 28, and so on). If the expressions are separated by semicolons, the printer prints each value with no space between. All numbers are printed with a trailing blank. If the number is negative, the sign precedes the number, otherwise a blank precedes the number. No blanks precede or follow strings. (Note: You may not substitute L? for LPRINT.) Examples LPRINT \"The total for \";A$;\" was \"; TT If AS contains the string \"April\" and TT contains the value 1332.44, this statement prints: The total for April was 1332.44 LPRINT X,Y,Z prints the value of X beginning in column 0, Y in column 14, and Z in column 28. LPRINT X,,Z prints the value of X beginning in column 0, and Z in column 42 (two columns are skipped because of the two commas.)
- Notes: This command formats and prints out the values of expression list using format string. For examples and a description of format string, see PRINT USING.
- Back: [index](#index)

<a id="kw-max"></a>
### MAX
- Variants: `MAX`
- Syntax: `MAX`
- Back: [index](#index)

<a id="kw-mdm"></a>
### MDM
- Variants: `MDM ON/OFF/STOP`
- Syntax: `MDM ON/OFF/STOP`
- Description: Enable/Disable Modem Interrupt
- Notes: This command enables or disables the ON MDM interrupt. ON enables the interrupt so that if a character is received via the modem, BASIC jumps to the subroutine defined in the ON MDM command. OFF disables the interrupt. STOP disables the interrupt, however, BASIC \"remembers\" that a character was received, so that if you issue a MDM ON command, BASIC jumps immediately to the interrupt subroutine. Examples 1A MDM ON enables the communications interrupt.
- Back: [index](#index)

<a id="kw-menu"></a>
### MENU
- Variants: `MENU`
- Syntax: `MENU`
- Description: Return to Menu
- Notes: MENU exits BASIC and returns you to the Model 100 Main Menu. If you were editing a current RAM filc, BASIC rewrites the file before returning to the Menu (unless you entered NEW before entering MENU). Example 1000 PRINT \"Press Any Key to Return to Menu\" 1010 A$ = INKEY$: IF A$ = \"\" GOTO 1010 1020 MENU prints the message and returns to the Menu when you press any key.
- Back: [index](#index)

<a id="kw-merge"></a>
### MERGE
- Variants: `MERGE`
- Syntax: `MERGE \"device: filename or configuration\"`
- Description: Merge Two Programs
- Notes: This command merges the lines from the ASCII formatted file called filename with the lines of the current program. If BASIC finds a duplicate line number, the line from filename replaces the current line. device may be RAM, CAS, COM, or MDM. If you don't specify a device, BASIC assumes RAM. filename consists of a string of one to six characters, the first of which is a letter. For RAM files, you may include the optional extension. DO; if omitted, BASIC assumes that extension. unless there is Basic file of same name. For example if there are \"PROG.DO\" and \"PROG.BA\", \"MERGE PROG\" will cause to merge PROG.BA, and result error. If device is CAS, then filename has no extension. filename is optional; if omitted, BASIC merges the first ASCII formatted cassette file it finds. For COM, configuration consists of a five character string of the pattern rwpbs, where: r r Baud Rate This is a number from 1 to 9, where 1=75; 2=110; 3=300; 4=600; 5=1200; 6=2400; 7=4800; 8=9600; 9=19200. w Word Length This is a number from 6 to 8, where 6=6 bits; 7=7 bits; 8=8 bits. p Parity Either E,O,I or N, where E=Even; O=Odd; I=Ignore; N=None. b Stop Bits Either 1 or 2, where 1=1 stop bit; 2=2 stop bits. s XON/XOFF Status Either E or D, where E=Enable; D=Disable. For MDM, configuration consists of a four character string of the pattern wpbs, defined above. (BASIC automatically sets the baud rate to 300 baud.) For information on storing files in ASCII format, see SAVE and CSAVE. Examples If the current program is: 10 FOR I=1 TO 100 20 PRINT AVE(I), BAL(I) 30 NEXT I and the file ACT.DO contains the lines: 20 PRINT CD$,BAL(I) 25 PRINT PD$ 40 MENU then after the command MERGE \"RAM:ACT.DO\" the current program reads: 10 FOR I=1 TO 10 20 PRINT CDS, BAL(I) 25 PRINT POS 30 NEXT I 40 MENU Other examples: MERGE \"CAS:ACCT\" merges the cassette file ACCT with the program in memory. MERGE \"COM:78e1e\" merges the file coming in on the RS-232C line with the program in memory. (Note: The party on the other end of the RS-232C line must send the ASCII-oriented file using the same configuration, after you enter the MERGE command.) MERGE \"MDM:8e1e\" merges the file coming in on the modem with the program in memory. (Note: The party on the other end of the phone line must send the ASCII-oriented file using the same configuration, after you enter the MERGE command.)
- Back: [index](#index)

<a id="kw-mid"></a>
### MID$
- Variants: `MID$`
- Syntax: `MID$(string expression, position, length)`; `MID$(string expression1,position,length) = string expression2`
- Description: Get Middle Characters of String Replace Middle Characters of a String
- Notes: This function returns length characters from string starting at position. length and position are numeric expressions. length is optional; if omitted, MID$ returns the entire portion of the string starting at position. Example 10 HASH$ = MID$(A$,2,2) If A$ contains the string \"00349953,\" then this statement assigns string \"34\" to HASH$.
- Notes: This MID$ replaces characters of string expression1, starting at position, with string expression2. length and position are numeric expressions. length is optional; if present it is ignored. string expression1 always keeps its original size, even if it means truncating string expression2 to fit. Example 10 MID$(A$,5) = \"FF\" If AS contains the string \"00000000,\" then this statement changes AS to \"0000FF00.\" 1000 MID$(A$,5) = \"ABCDEF\" If AS contains the string \"00000000,\" then this statement changes AS to \"0000ABCD.\"
- Back: [index](#index)

<a id="kw-mod"></a>
### MOD
- Variants: `MOD`
- Syntax: `expression MOD expression`
- Description: Modulo (remainder)
- Back: [index](#index)

<a id="kw-motor"></a>
### MOTOR
- Variants: `MOTOR`
- Syntax: `MOTOR ON or OFF`
- Description: Turn Cassette Motor On and Off
- Notes: MOTOR starts or stops the cassette recorder motor. Example MOTOR ON starts the cassette recorder motor.
- Back: [index](#index)

<a id="kw-name"></a>
### NAME
- Variants: `NAME...AS`, `NAME`
- Syntax: `NAME \"RAM:old filename\" AS \"RAM:new filename\"`; `NAME "ACCTS.DO" AS "OLDACT.DO"`
- Description: Rename a RAM file This command renames old filename to new filename.
- Notes: NAME renames a RAM file. old filename and new filename are strings of one to six characters, the first of which must be a letter, plus a two character extension. You must include the file's extension. Example NAME \"BILLS.BA\" AS \"ACCT.BA\" renames the file BILLS.BA to ACCT.BA.
- Notes: This command renames *old filename* to *new filename*. *old filename* and *new filename* consist of strings of one to six characters, the first of which must be a letter, plus the two character extension. You must include the extension, and you may not change extensions. *old filename* must already exist and *new filename* must not already exist. **RAM** is optional.  Examples  NAME "ACCTS.DO" AS "OLDACT.DO" renames the RAM file ACCTS.DO to OLDACT.DO.  10 INPUT "New filespec" ;FS$ 20 NAME "ACCTS.DO" AS FS$ renames ACCTS.DO to the input string FSS.
- Back: [index](#index)

<a id="kw-new"></a>
### NEW
- Variants: `NEW`
- Syntax: `NEW`
- Description: Erase the Current Program
- Notes: NEW, erases the current program, sets numeric variables equal to zero, and sets string variables equal to null (""). NEW does not change the string space allocation.  Example  NEW  deletes the current program.
- Back: [index](#index)

<a id="kw-next"></a>
### NEXT
- Variants: `NEXT`
- Description: See FOR...NEXT
- Back: [index](#index)

<a id="kw-not"></a>
### NOT
- Variants: `NOT`
- Syntax: `NOT expression`
- Description: Logical NOT
- Back: [index](#index)

<a id="kw-off"></a>
### OFF
- Variants: `OFF`
- Syntax: `OFF`
- Back: [index](#index)

<a id="kw-on"></a>
### ON
- Variants: `ON COM GOSUB`, `ON ERROR GOTO`, `ON KEY GOSUB`, `ON MDM GOSUB`, `ON TIME$ GOSUB`, `ON...GOTO`, `ON...GOSUB`
- Syntax: `ON COM GOSUB line number`; `ON ERROR GOTO line number`; `ON KEY GOSUB line number list`; `ON MDM GOSUB line number`; `ON TIMES$ = "time" GOSUB line number`; `ON numeric expression GOTO line number list`; `ON numeric expression GOSUB line number list`
- Description: Define Communications Interrupt Define Error Interrupt Define Function Key Interrupts Define Modem Interrupt Define Clock Interrupt Branch on Expression Branch on Expression
- Notes: This command defines a communications interrupt subroutine for incoming RS-232C communications. Once BASIC executes ON COM GOSUB, on receiving data over the RS-232C line, it branches to line number, regardless of where it currently is in the program. Normally, you'll put this command at the beginning of your program.  (Note: You must enable communications interrupt before it can interrupt the program. See COM ON for details.)  Example  10 ON COM GOSUB 1000 20 COM ON . . . 1000 OPEN "COM:78N1E" FOR INPUT AS 1 1010 OPEN "IMPDAT.DO" FOR OUTPUT AS 2 1020 LINE INPUT #1,A$ 1030 PRINT #2,A$ 1040 IF NOT EOF(1) THEN GOTO 1020 1050 CLOSE 1,2 1060 RETURN  defines a communications interrupt routine starting at line 1000. When data begins coming in on the RS-232C line, control transfers to line 1000, where it copies the input into a RAM file called "IMPDAT.DO".
- Notes: *ON ERROR* defines an error trapping interrupt. After executing this command, if an error occurs elsewhere in the program, BASIC immediately jumps to *line number*. Normally, the routine beginning at *line number* processes the error in some fashion. At the end of the routine, you must either terminate the program (*STOP* or *END*) or else return to the program with *RESUME*. See *STOP*, *END*, and *RESUME* for more details.  Example  100 ON ERROR GOTO 1000 ... 200 X = 10000 / Y ... 300 X = 300 / Y ... 1000 IF ERR<>11 THEN PRINT "Error Code";ERR;"in line ";ERL : STOP ELSE X=100000: RESUME NEXT  If an error occurs, BASIC jumps to line 1000. If the error was a division by zero (error #11), then X is set to a high value, 100000, and execution returns to the line following the error line. either line 200 or line 300. If some other error occurred, BASIC prints out the message and stops.
- Notes: This statement defines interrupts for the Function Keys. After executing this command, pressing the *nth* Function Key tells BASIC to jump to the *nth* line number in line number list. You may define as many of the Function Keys as you wish a BASIC ignores your pressing of undefined keys.  (Note: You must enable the Function Keys before they will interrupt the program. See KEY ON for details.)  Examples 10 ON KEY GOSUB 1000,2000,3000,,5000  defines an interrupt subroutine for Function Key 1, beginning at line 1000, an interrupt subroutine for Function Key 2, beginning at line 2000, an interrupt subroutine for Function Key 3, beginning at line 3000, and an interrupt subroutine for Function Key 5, beginning at line 5000. Function keys 4,6,7, and 8 are left undefined.
- Notes: This command defines an interrupt for incoming modem communications. Once BASIC executes ON MDM GOSUB, on receiving data over the modem, it branches to line number, regardless of where it currently is in the program. Normally, you'll put this command at the beginning of your program.  (Note: You must enable the modem interrupt before it can interrupt the program. See MDM ON for details.)  Example  10 ON MDM GOSUB 1000 defines a modem interrupt routine beginning at line 1000.
- Notes: This command defines an interrupt for a clock condition. time is a string expression of the form "HH:MM:SS." When TIMES equals time, BASIC calls the subroutine at line number, regardless of where it currently is in the program. Normally, you'll put this command at the beginning of your program.  (Note: You must enable the TIMES interrupt before it can interrupt the program. See TIMES ON for details.)  Example  10 ON TIME$ = "14:20:00" GOSUS 1000 defines a clock interrupt for 2:20 PM (14:20:00), beginning at line 1000.
- Notes: ON...GOTO evaluates numeric expression to an integer n, then branches to the nth line number in the list. numeric expression must evaluate to a non-negative number, which, if zero or greater than the number of line numbers in the list, tells BASIC to continue execution without branching.  Example  10 ON X GOTO 100,200,300  branches 10 100, 200 or 300, depending if X equals 1,2, or 3, respectively.
- Notes: ON...GOSUB evaluates numeric expression to an integer n, then calls the subroutine beginning at the nth line number in the list. numeric expression must evaluate to a non-negative number. which, if zero or greater than the number of line numbers in the list, tells BASIC to continue execution without branching.  Example  10 ON X GOSUB 100,200,300  calls the subroutine beginning at line 100,200 or 300, depending if X equals 1,2, or 3, respectively.
- Back: [index](#index)

<a id="kw-open"></a>
### OPEN
- Variants: `OPEN`
- Syntax: `OPEN "device:filename or configuration" FOR mode AS file number`
- Description: Open a File for I/O
- Notes: OPEN allocates a buffer for a file on the given device. device may be **RAM**, **CAS**, **COM**, **LCD**, **LPT**, or **MDM**. file number is the buffer nuinber assigned to the file. mode can be:  **OUTPUT** specifying data will be written sequentially to the file, starting at the beginning of the file  **INPUT** specifying data will be read sequentially from the file, starting at the beginning of the file  **APPEND** specifying that data will be written sequentially to the file, adding records to the end of the file  RAM Files: filename is a string of up to six characters, the first of which is a letter, plus a two character extension which must be .DO. mode can be OUTPUT, INPUT, or APPEND.  Cassette Files (CAS): filename is a string of up to six characters, the first of which is a letter. mode can be OUTPUT or INPUT.  Communications Files (COM): configuration consists of a five character string of the form rwpbs, where  r Baud Rate This is a number from 1 to 9, where 1=75, 2=110, 3=300; 4=600; 5=1200; 6=2400; 7=4800; 8=9600; 9=19200.  w Word Length This is a number from 6 to 8, where 6=6 bits; 7=7 bits; 8 = 8 bits.  p Parity Either E,O. or N, where E=even; O=odd; I=Ignore; N=none.  b Stop Bits Either 1 or 2, where 1=1 stop bit; 2=2 stop bits.  s XON/XOFF Status Either E or D, where E = enable; D=disable.  mode can be INPUT or OUTPUT.  Modem Files (MDM): configuration consists of a four character string of the pattern wpbs, defined above. (BASIC automatically sets the baud rate to 300 baud.) Screen Files (LCD): mode must be OUTPUT. There is no configuration. Printer Files (LPT): mode must be OUTPUT. There is no configuration. (Note: If your program uses more than one file at once, you must reset MAXFILES.)  Examples  10 OPEN "RAM:ACCT.DO" FOR APPEND AS 1 opens a RAM file called ACCT.DO for appending, and assigns it the file number "1."  10 OPEN "CAS:" FOR OUTPUT AS 3 opens an output file on cassette and assigns it to file number "3."  10 OPEN "COM:6601E" FOR INPUT AS 4 opens a communications file for input as file number 4, using 2400 baud, 6 bit words, odd parity. 1 stop bit, and line enable.  10 OPEN "MDM:6E1E" FOR INPUT AS 4 opens a modem file for input as file number 4, using 6 bit words, even parity. 1 stop bit, and line enable.  10 OPEN "LCD:" FOR OUTPUT AS 1 opens a screen file as file number 1.  10 OPEN "LPT:" FOR OUTPUT AS 1 opens a printer file as file number 1.
- Back: [index](#index)

<a id="kw-or"></a>
### OR
- Variants: `OR`
- Syntax: `expression OR expression`
- Description: Logical OR
- Back: [index](#index)

<a id="kw-out"></a>
### OUT
- Variants: `OUT`
- Syntax: `OUT port number, byte value`
- Description: Output a Byte to a CPU Port
- Notes: This command outputs byte value to port number. port number and byte value are numeric expressions in the range 0 to 255.  Example  10 OUT 55,100 outputs 100 to CPU port 55.
- Back: [index](#index)

<a id="kw-peek"></a>
### PEEK
- Variants: `PEEK`
- Syntax: `PEEK (memory address)`
- Description: Get a Value From Memory
- Notes: The PEEK function returns the byte value stored at memory address, memory address and the returned value are both in decimal form.  Example  10 A% = PEEK(16999)  assigns the byte value at address 16999 to A%.
- Back: [index](#index)

<a id="kw-poke"></a>
### POKE
- Variants: `POKE`
- Syntax: `POKE memory address, byte value`
- Description: Load a Value into Memory
- Notes: POKE loads memory address with byte value. Both must be expressed as decimal numeric expressions.  Example  100 POKE 60000, 104 loads 104 into address 60000.
- Back: [index](#index)

<a id="kw-pos"></a>
### POS
- Variants: `POS`
- Syntax: `POS (dummy numeric expression)`
- Description: Get Screen Position
- Notes: POS returns the current horizontal Screen position of the Cursor.  Example      100 OP% = POS(0)  assigns OP% the current horizontal cursor position.
- Back: [index](#index)

<a id="kw-power"></a>
### POWER
- Variants: `POWER`, `POWER CONT`, `POWER OFF`
- Syntax: `POWER numeric expression`; `POWER CONT`; `POWER OFF, RESUME`
- Description: Automatic Power Down Prevent Automatic Power Down Turn Off Power
- Notes: POWER sets the automatic power down period. numeric expression has a range of 10 to 255. The Model 100 will automatically turn off after a period of numeric expression x 0.1 minutes if you are neither running a program nor entering commands. The default value is 100 (10 minutes).  Example 10 POWER 10 sets the automatic power down period to one minute (10 X 0.1).
- Notes: This command disables the automatic power down feature of the Model 100.  Example  10 POWER CONT
- Notes: This turns off the power to the Model 100 immediately. RESUME is optional; if present, upon turning the power back on, the Model 100 resumes execution of the program at the statement following the POWER OFF,RESUME. If not present, then the Model 100 returns to the Main Menu upon power up.  Example  10 IF TIME$>"11:30:00" THEN POWER OFF turns off the power if the clock is past 11:30 AM. 20 POWER OFF,RESUME 30 PRINT "Starting Back Up"  turns off the power. When you turn the power back on, BASIC begins execution in line 30.
- Back: [index](#index)

<a id="kw-preset"></a>
### PRESET
- Variants: `PRESET`
- Syntax: `PRESET (x-coordinate, y-coordinate)`
- Description: Turn Off an LCD Pixel
- Notes: PRESET turns off the LCD pixel at (x-coordinate, y-coordinate). x-coordinate may range from 0 to 239, and y-coordinate may range from 0 to 63. See also PSET.  Example  10 PRESET (55,10)  turns off the pixel at (55,10).
- Back: [index](#index)

<a id="kw-print"></a>
### PRINT
- Variants: `PRINT`, `PRINT #`, `PRINT USING`, `PRINT # USING`
- Syntax: `PRINT expression list`; `PRINT # file number, expression list`; `PRINT USING "format"; expression list`; `PRINT #file number, USING "format"; expression list`
- Description: Print Data on the Screen Print to a File Formatted Print Formatted Print to a File
- Notes: This command prints the data in expression list onto the Screen, starting at the left-most end of the line. The items in expression list are separated by commas or semi-colons. If commas are used, the Cursor automatically advances to the next "print zone" before printing the next item. Print zones are at column 0 and column 14. If semi-colons are used, no space is inserted between the items printed on the display.  Positive numbers are printed with a leading blank and all numbers are printed with a trailing blank. Trailing zeroes to the right of the decimal point are not printed out.  No blanks are printed before or after strings. BASIC automatically moves the cursor to the next line after printing the expression list.  You may use a question mark ("?") as an abbreviation for the word PRINT.  # Examples  100 PRINT "Menu #";I prints MENU # followed immediately by the value of 1.  200 PRINT IZ,JZ,K prints the value of I% starting in column 0, J% in column 15, and K% in column O of the next line.
- Notes: PRINT # prints or transmits the values of expression list to the file opened as file number. The items in expression list are separated by commas or semi-colons. If commas are used, the Cursor automatically advances to the next "print zone" before printing the next item. Print zones are defined at columns 0, 15, 30, and so on. If semi-colons are used, no space is inserted between the items.  Positive numbers are printed with a leading blank and all numbers are printed with a trailing blank. Trailing zeroes to the right of the decimal point are not printed out. No blanks are printed before or after strings.  You may use a question mark ("?") as an abbreviation for the word PRINT.  Examples  100 OPEN "CAS:" FOR OUTPUT AS 1 . . 200 PRINT #1,A$  prints the value of A$ to a file on the cassette tape.  100 OPEN "COM:B7N1E" FOR OUTPUT AS 4 . . 200 PRINT #4,10,20,30  transmits the values 10, 20, and 30 out the RS-232C lines.
- Notes: This command prints the data in expression list using the specified format. The data items in expression list may be separated either by commas or semi-colons. format consists of one or more "field specifiers," which describe the type and format of the displayed data. If there are more data items in the list than given formats, BASIC reuses format starting at the left side of the string.  The field specifiers are:  "!" (String Data) Tells BASIC to print only the first character in the given string. PRINT USING "! "i"Tandy" T  "\n-spaces\" (String Data) Tells BASIC to print 2 + n characters from the string. If the two 's are typed with no spaces, two characters are printed; with one space, three characters are printed, and so on.  If the string is longer than the field, the extra characters are ignored. If the field is longer than the string, the string is left-justified in the field and padded with spaces on the right.  PRINT USING "\ \ "; "Tandy" Tand  # (Numeric Data) Specifies one digit position. Digit positions are always filled. If the number to be printed has fewer digits than position specified, the number will be right-justified (preceded by spaces) in the field, with spaces filled in on the left. If the number to be printed is larger than the specified field, BASIC prints out a "%" preceding the number.  PRINT USING "*****":5 5  + (Numeric Data) Inserts the algebraic sign of the number, either at the beginning or end of the number, depending on its occurrence in the format string  PRINT USING "+*****";-13 -13  PRINT USING "*****";14 14  - (Numeric Data) For negative numbers, inserts a minus sign either at the beginning or end of the number, depending on its occurrence in the format string. If the number is positive, then BASIC inserts a blank.  PRINT USING "-*****";14 14  PRINT USING "#*#**.**-";0.45 0.45  ** (Numeric Data) Changes any leading blanks to leading asterisks blanks. The ** also counts as two digit positions and must occur on the left side of the format string. PRINT USING "*****"; 145 ****145  $$ (Numeric Data) Prints a dollar sign to the immediate left of the formatted number. The $$ counts as two digit positions, one of which is the dollar sign and must be the first characters of the format string. You may not use the exponential format unless you specify a trailing minus sign. PRINT USING "$$*****";450 $450  **$ (Numeric Data) Fills leading spaces to asterisks except for the space to the immediate left of the number, where it inserts a dollar sign. **$ counts as three digit positions, one of which is the dollar sign. PRINT USING "**$***";12 ***$12  (Numeric Data) Inserts a decimal point. This specifier must be used as part of "#" field string. If the format string specifies that a digit is to precede the decimal point, the digit will always be printed (as 0 if necessary). Digits to the right of the decimal point are rounded as necessary. PRINT USING "****.##";14.5 14.50 PRINT USING "####.##";0.588 0.59  , (Numeric Data) Inserts a comma every three digits to the left of the decimal point. If the digit to the left of a potential comma is blank, then BASIC inserts a blank instead of the comma. The , must lie between numeric field specifiers (#,$ or **), to the left of the decimal point and counts as a digit position. PRINT USING "#########,";14432 14,432  ---- (Numeric Data) Specifies exponential format. The four carats count as four characters in the field and come after the numeric descriptors. Any decimal point position may be specified a the significant digits are left-justified, and the exponent is adjusted. Unless a leading + or trailing + or a is specified, one digit position will be used to the left of the decimal point to print a space or a minus sign. PRINT USING "****^^^^^";150000 E-0.4  (Note: The caret (^) is entered by pressing SHIFT 6, and the backslash (\) is entered by pressing GRPH -)  Examples  10 PRINT USING "\             \ ******,**##  ******,**"; A$,IBAL,OBAL  If A$ contains the string "Cramer.W.D", IBAL equals 1440.44, and OBAL equals 980.00, then this statement prints: Cramer.W.D 1.440.44 980.00 200 PRINT USING "*****..##";A,B,C  If A contains 34, B contains 44.323, and C contains 12333.33, then this statement prints out: $34.00 $44.32 $12333.33  Note that the blanks in the format string are significant.  In addition, characters other than the field specifiers are inserted as is, providing there is enough room in the field that BASIC doesn't try to use the characters for conversion. For example,  PRINT USING "$********,**";4534.34  prints: $ 4,534.34
- Notes: Formats the data in expression list and sends it to the device opened as file number. See PRINT # and PRINT USING for more information and examples.
- Back: [index](#index)

<a id="kw-pset"></a>
### PSET
- Variants: `PSET`
- Syntax: `PSET (x-coordinate,y-coordinate)`
- Description: Turn On LCD Pixels
- Notes: PSET turns on the LCD pixel at x-coordinate, y-coordinate, where x-coordinate is a numeric expression ranging from 0 to 239 and y-coordinate is a numeric expression ranging from 0 to 63.  Example  10 PSET (40,45)  turns on the pixel at 40,45.
- Back: [index](#index)

<a id="kw-read"></a>
### READ
- Variants: `READ`
- Syntax: `READ variable list`
- Description: Read Values From a DATA List
- Notes: This command reads an appropriate number of values from a DATA statement and stores the values in the variables of variable list. The values in the DATA statements must match in type (string or numeric) with the variables in variable list  The first time BASIC executes a READ command, the first value in the first DATA statement is used, the second time, the second value in the DATA statement is read, and so on. When all the items in the first DATA statement have been read, the next READ uses the first value in the second DATA statement, and so on.  To reuse the values of the DATA command, use the RESTORE command.  See also **DATA** and **RESTORE**.  Example  ``` 100 DATA 0.4, 0.2, "Trinity River" 120 READ A,B%,C$ ```  assigns A the value 0.4, B% the value 0.2, and C$ the string Trinity River.
- Back: [index](#index)

<a id="kw-rem"></a>
### REM
- Variants: `REM`
- Syntax: `REM comment statement`
- Description: Comment
- Notes: REM signifies to BASIC that the remainder of the line is a comment. Since BASIC ignores everything following REM, comment statement must be the last statement of the line.  You may abbreviate REM with an apostrophe. If the comment follows another BASIC command, then you must either use the ' or else precede REM with a colon.  Examples 10 REM This program finds the standard deviation 10 ' This program finds the standard deviation 100 AVE = SUM / TT 'Calculate the average 100 AVE = SUM / TT :REM Calculate the average
- Back: [index](#index)

<a id="kw-restore"></a>
### RESTORE
- Variants: `RESTORE`
- Syntax: `RESTORE line number`
- Description: Reset the DATA Statement Pointer
- Notes: This command resets the DATA statement pointer to the first item in the DATA statement on line number so that a READ command can access the same values more than once. line number is optional; if omitted, BASIC uses the first DATA statement.  See also DATA and READ.  Example 100 DATA "Nuts", "Bolts", "Screws", "Hammers" . . 300 READ ITEMS$(1), ITEMS$(2), ITEMS$(3), ITEMS$(4) . . 600 RESTORE 100 610 READ CT$(1), CT$(2), CT$(3), CT$(4)  Line 300 assigns the strings of the DATA statement in line 100 to ITEMS's 1 through 4. Line 600 resets the DATA pointer so that line 610 reassigns the strings to CTS's 1 through 4.
- Back: [index](#index)

<a id="kw-resume"></a>
### RESUME
- Variants: `RESUME`
- Syntax: `RESUME line number`
- Description: Resume Execution After an Error
- Notes: RESUME ends an error handling routine by branching to line number where BASIC begins normal execution. If line number is null or 0, then BASIC returns to the line which caused the error. You may also specify NEXT in which case BASIC returns to the line immediately following the error causing line.  Example 1000 IF ERR = 18 THEN PRINT @0, "Printer Not Ready!!!": RESUME 1010 .  If an I/O error occurs, then BASIC prints the message and resumes execution at the offending line. Otherwise, BASIC proceeds to line 1010.
- Back: [index](#index)

<a id="kw-return"></a>
### RETURN
- Variants: `RETURN`
- Syntax: `RETURN`
- Description: Returns from a subroutine
- Back: [index](#index)

<a id="kw-right"></a>
### RIGHT$
- Variants: `RIGHT$`
- Syntax: `RIGHT$ (string expression,count)`
- Description: Return Right Portion of a String
- Notes: RIGHTS returns the right-most count characters of string expression. count is a numeric expression.  Example  10 SEC$ = RIGHT$(TIME$,2) assigns the current second count to SEC$.
- Back: [index](#index)

<a id="kw-rnd"></a>
### RND
- Variants: `RND`
- Syntax: `RND (numeric expression)`
- Description: Return Pseudo-Random Number
- Notes: RND returns a pseudo-random number between 0 and 1. If numeric expression is non-zero, then RND returns a new random number. If numeric expression equals 0, then RND returns the last random number generated.  Example  20 PRINT RND(1) 30 PRINT RND(0)  Prints the same random number twice.  (Note: RND always generates the same random number series. If your application requires a different random number starting the sequence each time, you can use the clock to establish a starting point in the sequence. For example, the following routine points the random number generator to one of 60 starting points in the generator:  ``` 10 SEC = VAL(RIGHT$(TIME$,2)) 20 FOR I=1 TO SEC 30 DUMMY = RND(1) 40 NEXT I ```
- Back: [index](#index)

<a id="kw-run"></a>
### RUN
- Variants: `RUN`
- Syntax: `RUN "device:filename or configuration", R`; `RUN line number, R`
- Description: Execute a New BASIC Program Execute the Current BASIC Program
- Notes: RUN loads and runs a BASIC program from device. filename consists of a string of one to six characters, the first of which is a letter. device may be RAM, CAS, COM or MDM if device is RAM, then you may include the optional extension .BA or .DO. If device is CAS, then you use no extension.  For COM, configuration consists of a five character string of the pattern rwphs, where  r Baud Rate This is a number from 1 to 9, where 1=75; 2=110; 3=300; 4=600; 5=1200; 6=2400; 7=4800; 8=9600; 9=19200.  w Word Length This is a number from 6 to 8, where 6=6 bits. 7=7 bits; 8=8 bits.  p Parity Either E,O,I, or N, where E=Even: O=Odd; I=Ignore; N=None.  b Stop Bits Either 1 or 2. where 1=1 stop bit; 2=2 stop bits.  s XON/XOFF Status Either E or D, where E=Enable; D=Disable.  For MDM, configuration consists of a four character string of the pattern wpbs, defined above. (BASIC automatically sets the baud rate to 300 baud.)  R is optional; if present, it tells BASIC keep all open files opened. If omitted, BASIC closes any currently opened files before running the new program  Examples  1000 RUN "PART2.BA",R loads and executes the RAM file PART2.BA. keeping all open files open.  100 RUN "MDM:7EZE" loads and executes the BASIC program coming in over the modem lines.
- Notes: Run clears all variables and begins execution of the current program, starting at line number. line number is optional; if omitted, BASIC starts execution at the first line of the program. R. if present, tells BASIC to leave currently opened files open. If not present, BASIC closes all files before executing the program.  Examples RUN 100 Clears all variable values and starts executing the program at line 100. RUN,R  clears all numeric and string variables and begins execution of the current program. Open files are left open.
- Back: [index](#index)

<a id="kw-save"></a>
### SAVE
- Variants: `SAVE`
- Syntax: `SAVE "device:filename or configuration",A`
- Description: Save a BASIC Program
- Notes: SAVE writes the current BASIC program to the specified device. device may be RAM, CAS, COM, or MDM. filename consists of a string of 1 to 6 characters, the first of which is a letter. RAM filenames are optionally followed by the extension .BA or .DO. (if not present, BASIC adds an extension automatically)  The word RAM is also optional; if no device is named, BASIC assumes RAM. If filename already exists in RAM, BASIC writes over the old file. If device is CAS, there is no extension.  If device is COM, configuration consists of a five character string of the pattern rwpbs, where  *   **r** Baud Rate: This is a number from 1 to 9, where 1=75, 2=110; 3=300,     4=600; 5=1200; 6=2400; 7=4800; 8=9600, 9=19200 *   **w** Word Length: This is a number from 6 to 8, where 6=6 bits; 7=7 bits; 8=8 bits *   **p** Parity: Either E, O, I, or N, where E=Even; O=Odd; I=Ignore; N=None *   **b** Stop Bits: Either 1 or 2, where 1=1 stop bit, 2=2 stop bits. *   **s** XON/XOFF Status: Either E or D, where E=Enable; D=Disable.  If device is MDM, configuration consists of a four character string of the pattern wpbs, defined above. (BASIC automatically sets the baud rate to 300 baud.)  BASIC' requires no configuration or filename for LPT or LCD files.  A is optional; if present, BASIC saves the file in ASCII format. If not present, BASIC saves the file in a compressed format.  (Note: You must save BASIC files in ASCII format if you intend to merge them.) COM, MDM, LCD, and LPT all write the current program to their corresponding device in ASCII format.  Examples SAVE "TIMSET"  writes the current BASIC program to the RAM file TIMSET.BA. SAVE "PART3", A  writes the current BASIC program to the RAM file PART3.DO The file is stored in ASCII format. SAVE "CAS:CLOCK"  writes the current program to cassette tape naming the file CLOCK (identical to the command CSAVE "CLOCK"). SAVE "MDM:7N1E"  sends the current program out the modem, using the configuration 7 bit words. no parity check. 1 stop bit, and line enable. SAVE "COM:58E2E"  sends the current program out the RS-232C line using the configuration of 1200 baud, 8 bit words, even parity, 2 stop bits, and line enable. SAVE "LPT:"  writes the current program on the printer (identical to LLIST). SAVE "LCD:"  writes the current program to the Screen (identical to LIST).
- Back: [index](#index)

<a id="kw-screen"></a>
### SCREEN
- Variants: `SCREEN`
- Syntax: `SCREEN on/off`
- Description: Locks/Unlocks LABEL Line
- Notes: SCREEN locks or unlocks the bottom (LABEL) line on the Display for scrolling. on is 0.0 and off is 0.1.  Example SCREEN 0,0 causes the LABEL. line to disappear and allows you to scroll with all eight lines. SCREEN 0,1 causes the LABEL line to reappear.
- Back: [index](#index)

<a id="kw-sgn"></a>
### SGN
- Variants: `SGN`
- Syntax: `SGN(numeric expression)`
- Description: Algebraic Sign
- Notes: This expression returns a -1 for negative numbers, 0 for zero, and 1 for positive numbers.  Example  200 TTL = 10 * SGN(CR) sets TTL equal to either 10, 0, or -10, depending on whether CR is positive, zero, or negative.
- Back: [index](#index)

<a id="kw-sin"></a>
### SIN
- Variants: `SIN`
- Syntax: `SIN (numeric expression)`
- Description: Trigonometric Sine
- Notes: SIN returns (in radians) the trigonometric sine of numeric expression.  Example  100 Y = SIN(1.5) assigns Y the value 0.99749498660406.
- Back: [index](#index)

<a id="kw-sound"></a>
### SOUND
- Variants: `SOUND`, `SOUND ON/OFF`
- Syntax: `SOUND pitch, length`; `SOUND ON or OFF`
- Description: Output a Tone Enable/Disable Sound
- Notes: SOUND "plays" a given pitch for the given length. length ranges from 0 to 255. Dividing length by 50 gives the approximate length in seconds. pitch ranges from 0 to 16383, with the larger values corresponding to higher pitches. The values of pitch corresponding to musical notes are shown below.  Octave Note 1 2 3 4 5 G 12538 6269 3134 1567 783 G# 11836 5918 2959 1479 739 A 11172 5586 2793 1396 698 A# 10544 5272 2636 1318 659 B 9952 4976 2484 1244 622 C 9394 4697 2348 1174 587 C# 8866 4433 2216 1108 554 D 8368 4184 2092 1046 523 D# 7900 3950 1975 987 493 E 7456 3728 1864 932 466 F 7032 3516 1758 870 439 F# 6642 3321 1660 830 415
- Notes: SOUND ON tells BASIC to "beep" when: 1) You're loading from cassette. 2) The Model 100 is waiting on a carrier signal from the telephone modem lines.  SOUND OFF disables the "beep" under these circumstances. The cold start default is SOUND ON.  (Note: SOUND ON and SOUND OFF do not effect any of the other sound generating commands, such as BEEP and SOUND.)
- Back: [index](#index)

<a id="kw-space"></a>
### SPACE$
- Variants: `SPACE$`
- Syntax: `SPACE(length)`
- Description: String of Spaces
- Notes: This function returns a string of length spaces.  Example  100 B$ = SPACE$(20) + A$  sets B$ equal to a string of 20 spaces followed by the string stored in A$.
- Back: [index](#index)

<a id="kw-sqr"></a>
### SQR
- Variants: `SQR`
- Syntax: `SQR(numeric expression)`
- Description: Square Root
- Notes: SQR returns the square root of numeric expression, numeric expression must be a positive number.  Example  10 C = SQR(A^2 + B^2)  sets C equal to the square root of the sum of AA  and BA .
- Back: [index](#index)

<a id="kw-step"></a>
### STEP
- Variants: `STEP`
- Syntax: `STEP`
- Back: [index](#index)

<a id="kw-stop"></a>
### STOP
- Variants: `STOP`
- Syntax: `STOP`
- Description: Stop Execution
- Notes: STOP stops execution of a BASIC program at some point other than the physical end. STOP is primarily a "debugging" aid. By inserting STOP commands inside your program, you can examine or change the values of variables, and then resume execution of the program (with the CONT command) at the point following the STOP command.  Example  100 FOR I=1 TO 100 110 B$(I) = MN$ + DESC$(I) + MID$(TIME$,1,2) 111 STOP 120 NEXT I  stops execution of the program at line 111. Typing CONT will begin execution at line 120 (providing you have not altered the BASIC program).
- Back: [index](#index)

<a id="kw-str"></a>
### STR$
- Variants: `STR$`
- Syntax: `STRS(numeric expression)`
- Description: Convert a Number to a String
- Notes: STRS converts numeric expression to its string represention. This function is the inverse of VAL.  Example B$ = "$" + STR$(BAL) + ".00" If BAL contains the value 133, then this statement sets B$ equal to $133.00.
- Back: [index](#index)

<a id="kw-string"></a>
### STRING$
- Variants: `STRING$`
- Syntax: `STRING (length, character)`
- Description: Define a String of Characters
- Notes: STRING returns a string of the given length composed of character. length may range from 0 to 255. character is either a string expression or numeric expression; if it is a string expression, only the first character of the string is duplicated. If it is a numeric expression, it must evaluate to a number between 0 and 255.  Example  PRINT STRING$(20,"*") prints a string of 20 asterisks.  PRINT STRING$(40,239) prints a string of 40 solid blocks (239 is the ASCII code for a solid block).
- Back: [index](#index)

<a id="kw-tab"></a>
### TAB(
- Variants: `TAB(`
- Syntax: `TAB(`
- Back: [index](#index)

<a id="kw-tan"></a>
### TAN
- Variants: `TAN`
- Syntax: `TAN (numeric expression)`
- Description: Trigonometric Tangent
- Notes: TAN returns the tangent of numeric expression. numeric expression must be in radians.  Example  10 SLOPE = TAN (THETA)  assigns SLOPE the value of the tangent of THETA.
- Back: [index](#index)

<a id="kw-then"></a>
### THEN
- Variants: `THEN`
- Syntax: `IF condition THEN commands`
- Description: Used with IF to specify true branch
- Back: [index](#index)

<a id="kw-time"></a>
### TIME$
- Variants: `TIME$`
- Syntax: `TIME$`
- Description: Current Time
- Notes: TIME keeps track of the current time, in the form of a string variable. You may access it like any string variable, including resetting the time. The time string has the form "HH:MM:SS", where 00 a HH a 23, 00 a MM a 59, and 00 a SS a 59. BASIC automatically updates TIMES, including changing from 23:59:59 to 00:00:00.  (Note: BASIC allows values up to 29 for HH. However, such values have no meaning and prevent TIME from ever returning to 00:00:00.)  Examples  PRINT TIME$ prints the current time.  TIME$="10:00:00" sets the time to 10:00 AM.
- Back: [index](#index)

<a id="kw-to"></a>
### TO
- Variants: `TO`
- Syntax: `TO`
- Back: [index](#index)

<a id="kw-using"></a>
### USING
- Variants: `USING`
- Syntax: `USING`
- Back: [index](#index)

<a id="kw-val"></a>
### VAL
- Variants: `VAL`
- Syntax: `VAL (string expression)`
- Description: Convert Strings To Numbers
- Notes: VAL converts string expression to a numeric representation of the string. If string expression contains non-numeric characters, VAL returns only the value of the leading number, if any. VAL is the inverse of the function STR$.  Examples  5 B$ = "100.44824" 10 A = VAL(B$)  sets A equal to 100.44824.  5 B$ = "no balance" 10 A = VAL(B$)  sets A equal to 0.  5 B$ = "3.00313354E33" 10 A = VAL(B$)  sets A equal to 3.00313354 x 10^33.
- Back: [index](#index)

<a id="kw-varptr"></a>
### VARPTR
- Variants: `VARPTR`
- Syntax: `VARPTR (variable name)`
- Description: Get Address of a Variable
- Notes: VARPTR returns the memory address of variable name. If you haven't yet used variable name, then VARPTR causes an error condition. This function may be useful in conjunction with PEEK and POKE, as well as CALL. Note that the returning address is an integer value, expressed in decimal form, hence memory addresses over 32767 return negative values.  Example LINK(I) = VARPTR (B$) sets LINK(I) equal to the memory address of B$.
- Back: [index](#index)

<a id="kw-width"></a>
### WIDTH
- Variants: `WIDTH`
- Syntax: `WIDTH`
- Back: [index](#index)

<a id="kw-xor"></a>
### XOR
- Variants: `XOR`
- Syntax: `expression XOR expression`
- Description: Logical XOR
- Back: [index](#index)

<a id="kw-symbol-126"></a>
### \
- Variants: `\`
- Syntax: `\`
- Back: [index](#index)

<a id="kw-symbol-127"></a>
### ^
- Variants: `^`
- Syntax: `^`
- Back: [index](#index)