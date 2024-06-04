library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity cache_memory is
    port (
        clk         : in  std_logic;
        reset       : in  std_logic;
        cpu_address : in  std_logic_vector(31 downto 0); -- CPU address (assume 32-bit)
        cpu_read    : in  std_logic;                     -- CPU read request
        cpu_data_out: out std_logic_vector(63 downto 0); -- 64-bit data output to CPU

        ram_address : out std_logic_vector(31 downto 0); -- Address output to RAM
        ram_data_in : in  std_logic_vector(31 downto 0); -- 32-bit data input from RAM
        ram_read    : out std_logic                      -- Read enable signal to RAM
    );
end entity cache_memory;

architecture rtl of cache_memory is
    -- Constants
    constant PAGE_SIZE    : integer := 1024; -- Size of a page in bits
    constant WORDS_PER_PAGE : integer := PAGE_SIZE / 32; -- Number of 32-bit words per page
    constant CACHE_LINES  : integer := 4;    -- Number of cache lines (pages)

    -- Types
    type cache_line_type is record
        valid : std_logic;
        tag   : std_logic_vector(26 downto 0); -- Tag bits (32 - 2 (address) - 3 (word offset))
        data  : std_logic_vector(PAGE_SIZE-1 downto 0);
    end record;
    type cache_array_type is array (0 to CACHE_LINES-1) of cache_line_type;

    -- Signals
    signal cache         : cache_array_type;
    signal cache_address : std_logic_vector(1 downto 0); -- Address within the cache (2 bits)
    signal word_offset   : std_logic_vector(2 downto 0); -- Word offset within a page (3 bits)
    signal cache_hit     : std_logic;
    signal output_word   : std_logic_vector(31 downto 0); -- Temporary 32-bit word output
    signal ram_read_int  : std_logic;                      -- Intermediate signal for ram_read

begin

    -- Address decoding
    cache_address <= cpu_address(3 downto 2); -- Extract cache address bits
    word_offset   <= cpu_address(4 downto 2); -- Extract word offset bits

    -- Cache hit logic
    cache_hit <= '1' when cache(to_integer(unsigned(cache_address))).valid = '1' and
                        cache(to_integer(unsigned(cache_address))).tag = cpu_address(31 downto 5)
                else '0';

    -- RAM control process
    process (clk, reset)
    begin
        if reset = '1' then
            ram_read_int <= '0';
        elsif rising_edge(clk) then
            if cpu_read = '1' and cache_hit = '0' then -- Cache miss, read from RAM
                ram_read_int <= '1';
                ram_address <= cpu_address(31 downto 5) & "00000"; -- Page address in RAM
            else
                ram_read_int <= '0';
            end if;
        end if;
    end process;

    -- Cache data loading process
    process (clk, reset)
    begin
        if reset = '1' then
            for i in cache'range loop
                cache(i).valid <= '0';
            end loop;
        elsif rising_edge(clk) then
            if ram_read_int = '1' then -- Loading data from RAM
                cache(to_integer(unsigned(cache_address))).data((to_integer(unsigned(word_offset))+1)*32-1 downto to_integer(unsigned(word_offset))*32) <= ram_data_in;
                if word_offset = "111" then -- Last word of the page loaded
                    cache(to_integer(unsigned(cache_address))).valid <= '1';
                    cache(to_integer(unsigned(cache_address))).tag   <= cpu_address(31 downto 5);
                end if;
            end if;
        end if;
    end process;

    -- Data output to CPU
    process (clk)
    begin
        if rising_edge(clk) then
            if cpu_read = '1' then
                if cache_hit = '1' then
                    output_word <= cache(to_integer(unsigned(cache_address))).data((to_integer(unsigned(word_offset))+1)*32-1 downto to_integer(unsigned(word_offset))*32);
                else
                    output_word <= (others => '0'); -- Default output on cache miss (can be improved)
                end if;
            end if;
        end if;
    end process;

    -- Assemble 64-bit output from two 32-bit words
    cpu_data_out <= cache(to_integer(unsigned(cache_address))).data((to_integer(unsigned(word_offset))+2)*32-1 downto (to_integer(unsigned(word_offset))+1)*32) & output_word;

    -- Assign intermediate signal to output port
    ram_read <= ram_read_int;

end architecture rtl;