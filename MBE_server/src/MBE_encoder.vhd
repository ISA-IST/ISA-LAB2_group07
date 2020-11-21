LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_arith.all;

ENTITY MBE_encoder IS
PORT( 	
		-- b_2j+1, b_2j, b_2j-1
		b2, b1, b0: IN STD_LOGIC;
		A: IN STD_LOGIC_VECTOR(31 downto 0);
		pp: OUT STD_LOGIC_VECTOR(32 downto 0)
);
END ENTITY;

ARCHITECTURE beh OF MBE_encoder IS

	COMPONENT mux_4to1_nbit IS
	GENERIC ( N : POSITIVE :=1
	);
	PORT( 
		I0, I1, I2, I3: IN SIGNED(N-1 downto 0);
		SEL  : IN STD_LOGIC_VECTOR(1 downto 0);
		O    : OUT SIGNED(N-1 downto 0)
	);
	END COMPONENT;
	
	-- mux selectors
	SIGNAL s: STD_LOGIC_VECTOR(1 downto 0);
	
	SIGNAL q: STD_LOGIC_VECTOR(32 downto 0);
	
BEGIN

	s(0) <= b2 XOR b1;
	s(1) <= b1 XOR b0;
	
	mux: mux_4to1_nbit GENERIC MAP(N=>33) PORT MAP(I0 => (OTHERS=>'0'), I1 => A & '0', I2 => '0' & A, I3 => '0' & A, O => q); 
	
	
	-- inverting of q if b_2j+1 is 1 cause it means that the pp is negative
	-- the sum of the 1 at the lsb position is performed in the tree
	pp <= q XOR (OTHERS=>b2);
	
END beh;
	
