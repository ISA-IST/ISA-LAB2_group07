library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
use ieee.std_logic_textio.all;

library std;
use std.textio.all;

entity data_maker is
  port (
    CLK  : in  std_logic;
    DATA_a, DATA_b : out std_logic_vector(31 downto 0));
end data_maker;

architecture beh of data_maker is

begin  -- beh

  process (CLK)
    file fp : text open read_mode is "./tb/fp_samples.hex";
    file m_b : text open read_mode is "./tb/B_mult.hex";
    file sq: text open write_mode is "./tb/square_res.hex";
    variable ptr_sq: line;
    variable ptr : line;
    variable val : std_logic_vector(31 downto 0);
    variable ptr_b : line;
    variable val_b : std_logic_vector(31 downto 0);
    variable val_square_tmp: unsigned(63 downto 0);
    variable val_square: std_logic_vector(63 downto 0);
  begin  -- process
    if CLK'event and CLK = '1' then  -- rising clock edge
      if (not(endfile(fp))) then
        readline(fp, ptr);
        hread(ptr, val);        
      end if;
      if (not(endfile(m_b))) then
        readline(m_b, ptr_b);
        hread(ptr_b, val_b);        
      end if;
      DATA_a <= val;
      DATA_b <= val_b;
      val_square_tmp := unsigned(val) * unsigned(val_b);
      val_square := std_logic_vector(val_square_tmp); 
      hwrite(ptr_sq, val_square);
      writeline(sq, ptr_sq);
    end if;
  end process;

end beh;
