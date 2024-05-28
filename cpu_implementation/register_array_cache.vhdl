library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity register_array_cache is
    -- No need for NUM_PAGES generic here
    generic (
        PAGE_SIZE : natural := 1024  -- Size of each page in bytes
    );
    port (
        clk     : in  std_logic;                     -- Clock input
        reset   : in  std_logic;                     -- Reset input
        address : in  std_logic_vector(1 downto 0);   -- Address input (2 bits for 4 pages)
        data_in : in  std_logic_vector(PAGE_SIZE-1 downto 0);  -- Data input
        read    : in  std_logic;                     -- Read enable input
        write   : in  std_logic;                     -- Write enable input
        data_out: out std_logic_vector(PAGE_SIZE-1 downto 0)  -- Data output
    );
end entity register_array_cache;

architecture rtl of register_array_cache is
    -- Directly define the array with 4 elements
    type page_array is array (0 to 3) of std_logic_vector(PAGE_SIZE-1 downto 0);
    signal cache : page_array;

begin
    process (clk, reset)
    begin
        if reset = '1' then
            -- Reset cache to all zeros
            for i in cache'range loop
                cache(i) <= (others => '0');
            end loop;
        elsif rising_edge(clk) then
            if write = '1' then
                -- Write data to the specified page
                cache(to_integer(unsigned(address))) <= data_in; 
            elsif read = '1' then
                -- Read data from the specified page
                data_out <= cache(to_integer(unsigned(address))); 
            end if;
        end if;
    end process;
end architecture rtl;