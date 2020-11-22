library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
use ieee.std_logic_textio.all;
use ieee.numeric_std.all;

library std;
use std.textio.all;

entity data_maker is
  port (
    CLK  : in  std_logic;
    b2, b1, b0: out std_logic;
    A: out std_logic_vector(31 downto 0));
end data_maker;

architecture beh of data_maker is

begin  -- beh

  process (CLK)
--    file fp : text open read_mode is "./tb/fp_samples.hex";
--    variable ptr : line;
--    variable val : std_logic_vector(31 downto 0);
    variable cnt : integer range 0 to 7 := 0;
    variable b: std_logic_vector(2 downto 0);
      
  begin  -- process
    if CLK'event and CLK = '1' then  -- rising clock edge
     -- if (not(endfile(fp))) then
     --   readline(fp, ptr);
     --   hread(ptr, val);        
     -- end if;
      if cnt = 7 then
         cnt := 0;
      else
         cnt := cnt + 1;
      
      end if;
      b := std_logic_vector(to_unsigned(cnt, 3));
    end if;
    b0 <= b(0);
    b1 <= b(1);
    b2 <= b(2);
  end process;

  A <= std_logic_vector(to_unsigned(5789112, 32));
  
end beh;
