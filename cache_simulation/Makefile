# Compiler & Flags 
CXX = g++
CXXFLAGS = -std=c++20 -Wall -Wextra -Werror -pedantic -O3

# Source, Object, & Executable 
SRCDIR = src
BUILDDIR = build
BINDIR = bin
EXE = $(BINDIR)/cache_simulation
SOURCES = $(wildcard $(SRCDIR)/*.cpp)
OBJECTS = $(patsubst $(SRCDIR)/%.cpp, $(BUILDDIR)/%.o, $(SOURCES))

# Ensure build directory
$(BUILDDIR):
	mkdir -p $(BUILDDIR)

$(BINDIR):
	mkdir -p $(BINDIR)
	
# Build targets
.PHONY: all clean run

all: $(EXE)

$(EXE): $(OBJECTS) | $(BINDIR)
	$(CXX) $(CXXFLAGS) $^ -o $@

$(BUILDDIR)/%.o: $(SRCDIR)/%.cpp | $(BUILDDIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	$(RM) -r $(BUILDDIR) $(BINDIR)

run:
	./$(EXE)