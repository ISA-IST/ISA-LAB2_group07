
LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_arith.all;

ENTITY dadda_tree IS
PORT (
	pp0, pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9,
	pp10, pp11, pp12, pp13, pp14, pp15: IN STD_LOGIC_VECTOR(32 downto 0);
	pp16: IN STD_LOGIC_VECTOR(31 downto 0);
	addend1_out, addend2_out: OUT STD_LOGIC_VECTOR(62 downto 0);
	M_lsb: OUT STD_LOGIC
);
END dadda_tree;

ARCHITECTURE struct OF dadda_tree IS

	COMPONENT FA IS
	PORT(
		a, b, c_in : IN std_logic;
		s, c_out : OUT std_logic);
	END COMPONENT;

	COMPONENT HA IS
	PORT(
		a, b : IN std_logic;
		s, c_out : OUT std_logic);
	END COMPONENT;

