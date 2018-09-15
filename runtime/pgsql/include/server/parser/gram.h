
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     IDENT = 258,
     FCONST = 259,
     SCONST = 260,
     BCONST = 261,
     XCONST = 262,
     Op = 263,
     ICONST = 264,
     PARAM = 265,
     TYPECAST = 266,
     DOT_DOT = 267,
     COLON_EQUALS = 268,
     EQUALS_GREATER = 269,
     LESS_EQUALS = 270,
     GREATER_EQUALS = 271,
     NOT_EQUALS = 272,
     ABORT_P = 273,
     ABSOLUTE_P = 274,
     ACCESS = 275,
     ACTION = 276,
     ADD_P = 277,
     ADMIN = 278,
     AFTER = 279,
     AGGREGATE = 280,
     ALL = 281,
     ALSO = 282,
     ALTER = 283,
     ALWAYS = 284,
     ANALYSE = 285,
     ANALYZE = 286,
     AND = 287,
     ANY = 288,
     ARRAY = 289,
     AS = 290,
     ASC = 291,
     ASSERTION = 292,
     ASSIGNMENT = 293,
     ASYMMETRIC = 294,
     AT = 295,
     ATTRIBUTE = 296,
     AUTHORIZATION = 297,
     BACKWARD = 298,
     BEFORE = 299,
     BEGIN_P = 300,
     BETWEEN = 301,
     BIGINT = 302,
     BINARY = 303,
     BIT = 304,
     BOOLEAN_P = 305,
     BOTH = 306,
     BY = 307,
     CACHE = 308,
     CALLED = 309,
     CASCADE = 310,
     CASCADED = 311,
     CASE = 312,
     CAST = 313,
     CATALOG_P = 314,
     CHAIN = 315,
     CHAR_P = 316,
     CHARACTER = 317,
     CHARACTERISTICS = 318,
     CHECK = 319,
     CHECKPOINT = 320,
     CLASS = 321,
     CLOSE = 322,
     CLUSTER = 323,
     COALESCE = 324,
     COLLATE = 325,
     COLLATION = 326,
     COLUMN = 327,
     COMMENT = 328,
     COMMENTS = 329,
     COMMIT = 330,
     COMMITTED = 331,
     CONCURRENTLY = 332,
     CONFIGURATION = 333,
     CONFLICT = 334,
     CONNECTION = 335,
     CONSTRAINT = 336,
     CONSTRAINTS = 337,
     CONTENT_P = 338,
     CONTINUE_P = 339,
     CONVERSION_P = 340,
     COPY = 341,
     COST = 342,
     CREATE = 343,
     CROSS = 344,
     CSV = 345,
     CUBE = 346,
     CURRENT_P = 347,
     CURRENT_CATALOG = 348,
     CURRENT_DATE = 349,
     CURRENT_ROLE = 350,
     CURRENT_SCHEMA = 351,
     CURRENT_TIME = 352,
     CURRENT_TIMESTAMP = 353,
     CURRENT_USER = 354,
     CURSOR = 355,
     CYCLE = 356,
     DATA_P = 357,
     DATABASE = 358,
     DAY_P = 359,
     DEALLOCATE = 360,
     DEC = 361,
     DECIMAL_P = 362,
     DECLARE = 363,
     DEFAULT = 364,
     DEFAULTS = 365,
     DEFERRABLE = 366,
     DEFERRED = 367,
     DEFINER = 368,
     DELETE_P = 369,
     DELIMITER = 370,
     DELIMITERS = 371,
     DEPENDS = 372,
     DESC = 373,
     DICTIONARY = 374,
     DISABLE_P = 375,
     DISCARD = 376,
     DISTINCT = 377,
     DO = 378,
     DOCUMENT_P = 379,
     DOMAIN_P = 380,
     DOUBLE_P = 381,
     DROP = 382,
     EACH = 383,
     ELSE = 384,
     ENABLE_P = 385,
     ENCODING = 386,
     ENCRYPTED = 387,
     END_P = 388,
     ENUM_P = 389,
     ESCAPE = 390,
     EVENT = 391,
     EXCEPT = 392,
     EXCLUDE = 393,
     EXCLUDING = 394,
     EXCLUSIVE = 395,
     EXECUTE = 396,
     EXISTS = 397,
     EXPLAIN = 398,
     EXTENSION = 399,
     EXTERNAL = 400,
     EXTRACT = 401,
     FALSE_P = 402,
     FAMILY = 403,
     FETCH = 404,
     FILTER = 405,
     FIRST_P = 406,
     FLOAT_P = 407,
     FOLLOWING = 408,
     FOR = 409,
     FORCE = 410,
     FOREIGN = 411,
     FORWARD = 412,
     FREEZE = 413,
     FROM = 414,
     FULL = 415,
     FUNCTION = 416,
     FUNCTIONS = 417,
     GLOBAL = 418,
     GRANT = 419,
     GRANTED = 420,
     GREATEST = 421,
     GROUP_P = 422,
     GROUPING = 423,
     HANDLER = 424,
     HAVING = 425,
     HEADER_P = 426,
     HOLD = 427,
     HOUR_P = 428,
     IDENTITY_P = 429,
     IF_P = 430,
     ILIKE = 431,
     IMMEDIATE = 432,
     IMMUTABLE = 433,
     IMPLICIT_P = 434,
     IMPORT_P = 435,
     IN_P = 436,
     INCLUDING = 437,
     INCREMENT = 438,
     INDEX = 439,
     INDEXES = 440,
     INHERIT = 441,
     INHERITS = 442,
     INITIALLY = 443,
     INLINE_P = 444,
     INNER_P = 445,
     INOUT = 446,
     INPUT_P = 447,
     INSENSITIVE = 448,
     INSERT = 449,
     INSTEAD = 450,
     INT_P = 451,
     INTEGER = 452,
     INTERSECT = 453,
     INTERVAL = 454,
     INTO = 455,
     INVOKER = 456,
     IS = 457,
     ISNULL = 458,
     ISOLATION = 459,
     JOIN = 460,
     KEY = 461,
     LABEL = 462,
     LANGUAGE = 463,
     LARGE_P = 464,
     LAST_P = 465,
     LATERAL_P = 466,
     LEADING = 467,
     LEAKPROOF = 468,
     LEAST = 469,
     LEFT = 470,
     LEVEL = 471,
     LIKE = 472,
     LIMIT = 473,
     LISTEN = 474,
     LOAD = 475,
     LOCAL = 476,
     LOCALTIME = 477,
     LOCALTIMESTAMP = 478,
     LOCATION = 479,
     LOCK_P = 480,
     LOCKED = 481,
     LOGGED = 482,
     MAPPING = 483,
     MATCH = 484,
     MATERIALIZED = 485,
     MAXVALUE = 486,
     METHOD = 487,
     MINUTE_P = 488,
     MINVALUE = 489,
     MODE = 490,
     MONTH_P = 491,
     MOVE = 492,
     NAME_P = 493,
     NAMES = 494,
     NATIONAL = 495,
     NATURAL = 496,
     NCHAR = 497,
     NEXT = 498,
     NO = 499,
     NONE = 500,
     NOT = 501,
     NOTHING = 502,
     NOTIFY = 503,
     NOTNULL = 504,
     NOWAIT = 505,
     NULL_P = 506,
     NULLIF = 507,
     NULLS_P = 508,
     NUMERIC = 509,
     OBJECT_P = 510,
     OF = 511,
     OFF = 512,
     OFFSET = 513,
     OIDS = 514,
     ON = 515,
     ONLY = 516,
     OPERATOR = 517,
     OPTION = 518,
     OPTIONS = 519,
     OR = 520,
     ORDER = 521,
     ORDINALITY = 522,
     OUT_P = 523,
     OUTER_P = 524,
     OVER = 525,
     OVERLAPS = 526,
     OVERLAY = 527,
     OWNED = 528,
     OWNER = 529,
     PARALLEL = 530,
     PARSER = 531,
     PARTIAL = 532,
     PARTITION = 533,
     PASSING = 534,
     PASSWORD = 535,
     PLACING = 536,
     PLANS = 537,
     POLICY = 538,
     POSITION = 539,
     PRECEDING = 540,
     PRECISION = 541,
     PRESERVE = 542,
     PREPARE = 543,
     PREPARED = 544,
     PRIMARY = 545,
     PRIOR = 546,
     PRIVILEGES = 547,
     PROCEDURAL = 548,
     PROCEDURE = 549,
     PROGRAM = 550,
     QUOTE = 551,
     RANGE = 552,
     READ = 553,
     REAL = 554,
     REASSIGN = 555,
     RECHECK = 556,
     RECURSIVE = 557,
     REF = 558,
     REFERENCES = 559,
     REFRESH = 560,
     REINDEX = 561,
     RELATIVE_P = 562,
     RELEASE = 563,
     RENAME = 564,
     REPEATABLE = 565,
     REPLACE = 566,
     REPLICA = 567,
     RESET = 568,
     RESTART = 569,
     RESTRICT = 570,
     RETURNING = 571,
     RETURNS = 572,
     REVOKE = 573,
     RIGHT = 574,
     ROLE = 575,
     ROLLBACK = 576,
     ROLLUP = 577,
     ROW = 578,
     ROWS = 579,
     RULE = 580,
     SAVEPOINT = 581,
     SCHEMA = 582,
     SCROLL = 583,
     SEARCH = 584,
     SECOND_P = 585,
     SECURITY = 586,
     SELECT = 587,
     SEQUENCE = 588,
     SEQUENCES = 589,
     SERIALIZABLE = 590,
     SERVER = 591,
     SESSION = 592,
     SESSION_USER = 593,
     SET = 594,
     SETS = 595,
     SETOF = 596,
     SHARE = 597,
     SHOW = 598,
     SIMILAR = 599,
     SIMPLE = 600,
     SKIP = 601,
     SMALLINT = 602,
     SNAPSHOT = 603,
     SOME = 604,
     SQL_P = 605,
     STABLE = 606,
     STANDALONE_P = 607,
     START = 608,
     STATEMENT = 609,
     STATISTICS = 610,
     STDIN = 611,
     STDOUT = 612,
     STORAGE = 613,
     STRICT_P = 614,
     STRIP_P = 615,
     SUBSTRING = 616,
     SYMMETRIC = 617,
     SYSID = 618,
     SYSTEM_P = 619,
     TABLE = 620,
     TABLES = 621,
     TABLESAMPLE = 622,
     TABLESPACE = 623,
     TEMP = 624,
     TEMPLATE = 625,
     TEMPORARY = 626,
     TEXT_P = 627,
     THEN = 628,
     TIME = 629,
     TIMESTAMP = 630,
     TO = 631,
     TRAILING = 632,
     TRANSACTION = 633,
     TRANSFORM = 634,
     TREAT = 635,
     TRIGGER = 636,
     TRIM = 637,
     TRUE_P = 638,
     TRUNCATE = 639,
     TRUSTED = 640,
     TYPE_P = 641,
     TYPES_P = 642,
     UNBOUNDED = 643,
     UNCOMMITTED = 644,
     UNENCRYPTED = 645,
     UNION = 646,
     UNIQUE = 647,
     UNKNOWN = 648,
     UNLISTEN = 649,
     UNLOGGED = 650,
     UNTIL = 651,
     UPDATE = 652,
     USER = 653,
     USING = 654,
     VACUUM = 655,
     VALID = 656,
     VALIDATE = 657,
     VALIDATOR = 658,
     VALUE_P = 659,
     VALUES = 660,
     VARCHAR = 661,
     VARIADIC = 662,
     VARYING = 663,
     VERBOSE = 664,
     VERSION_P = 665,
     VIEW = 666,
     VIEWS = 667,
     VOLATILE = 668,
     WHEN = 669,
     WHERE = 670,
     WHITESPACE_P = 671,
     WINDOW = 672,
     WITH = 673,
     WITHIN = 674,
     WITHOUT = 675,
     WORK = 676,
     WRAPPER = 677,
     WRITE = 678,
     XML_P = 679,
     XMLATTRIBUTES = 680,
     XMLCONCAT = 681,
     XMLELEMENT = 682,
     XMLEXISTS = 683,
     XMLFOREST = 684,
     XMLPARSE = 685,
     XMLPI = 686,
     XMLROOT = 687,
     XMLSERIALIZE = 688,
     YEAR_P = 689,
     YES_P = 690,
     ZONE = 691,
     NOT_LA = 692,
     NULLS_LA = 693,
     WITH_LA = 694,
     POSTFIXOP = 695,
     UMINUS = 696
   };
#endif



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
{

/* Line 1676 of yacc.c  */
#line 192 "src/backend/parser/gram.y"

	core_YYSTYPE		core_yystype;
	/* these fields must match core_YYSTYPE: */
	int					ival;
	char				*str;
	const char			*keyword;

	char				chr;
	bool				boolean;
	JoinType			jtype;
	DropBehavior		dbehavior;
	OnCommitAction		oncommit;
	List				*list;
	Node				*node;
	Value				*value;
	ObjectType			objtype;
	TypeName			*typnam;
	FunctionParameter   *fun_param;
	FunctionParameterMode fun_param_mode;
	FuncWithArgs		*funwithargs;
	DefElem				*defelt;
	SortBy				*sortby;
	WindowDef			*windef;
	JoinExpr			*jexpr;
	IndexElem			*ielem;
	Alias				*alias;
	RangeVar			*range;
	IntoClause			*into;
	WithClause			*with;
	InferClause			*infer;
	OnConflictClause	*onconflict;
	A_Indices			*aind;
	ResTarget			*target;
	struct PrivTarget	*privtarget;
	AccessPriv			*accesspriv;
	struct ImportQual	*importqual;
	InsertStmt			*istmt;
	VariableSetStmt		*vsetstmt;



/* Line 1676 of yacc.c  */
#line 535 "src/backend/parser/gram.h"
} YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif



#if ! defined YYLTYPE && ! defined YYLTYPE_IS_DECLARED
typedef struct YYLTYPE
{
  int first_line;
  int first_column;
  int last_line;
  int last_column;
} YYLTYPE;
# define yyltype YYLTYPE /* obsolescent; will be withdrawn */
# define YYLTYPE_IS_DECLARED 1
# define YYLTYPE_IS_TRIVIAL 1
#endif



