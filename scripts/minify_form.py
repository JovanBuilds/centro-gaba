import re

def main():
    path = "src/pages/index.astro"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Form specific wrapper modifications
    content = content.replace(
        'class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10"',
        'class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10"'
    )
    content = content.replace(
        'class="bg-[var(--color-gaba-surface)] rounded-3xl shadow-2xl overflow-hidden p-8 md:p-12 transition-colors duration-300"',
        'class="bg-[var(--color-gaba-surface)] rounded-2xl md:rounded-3xl shadow-2xl overflow-hidden p-5 sm:p-8 md:p-12 transition-colors duration-300"'
    )
    content = content.replace(
        'class="text-3xl md:text-4xl font-bold text-[var(--color-gaba-blue)] mb-4"',
        'class="text-2xl sm:text-3xl md:text-4xl font-bold text-[var(--color-gaba-blue)] mb-2 sm:mb-4 tracking-tight"'
    )
    content = content.replace(
        'class="text-lg text-[var(--color-gaba-navy)]/70"',
        'class="text-sm sm:text-lg text-[var(--color-gaba-navy)]/70 px-2 sm:px-0"'
    )
    content = content.replace(
        'class="mb-8 p-6 bg-[var(--color-gaba-blue)]/5 border-l-4 border-[var(--color-gaba-blue)] rounded-r-xl"',
        'class="mb-6 sm:mb-8 p-4 sm:p-6 bg-[var(--color-gaba-blue)]/5 border-l-[3px] sm:border-l-4 border-[var(--color-gaba-blue)] rounded-r-lg sm:rounded-r-xl"'
    )
    content = content.replace(
        'class="text-[var(--color-gaba-navy)] leading-relaxed"',
        'class="text-xs sm:text-base text-[var(--color-gaba-navy)] leading-relaxed"'
    )
    content = content.replace(
        'class="space-y-10"',
        'class="space-y-6 sm:space-y-10"'
    )

    # General replacements inside the form
    # 1. Input Base
    content = content.replace(
        'class="w-full px-4 py-3 rounded-xl border border-[var(--color-gaba-border)] focus:ring-2 focus:ring-[var(--color-gaba-blue)] focus:border-transparent outline-none transition-all bg-[var(--color-gaba-surface-alt)] focus:bg-[var(--color-gaba-surface)] text-[var(--color-gaba-navy)]"',
        'class="w-full px-3 py-2.5 sm:px-4 sm:py-3 text-sm sm:text-base rounded-lg sm:rounded-xl border border-[var(--color-gaba-border)] focus:ring-2 focus:ring-[var(--color-gaba-blue)] focus:border-transparent outline-none transition-all bg-[var(--color-gaba-surface-alt)] focus:bg-[var(--color-gaba-surface)] text-[var(--color-gaba-navy)]"'
    )
    # 1.5. textarea
    content = content.replace(
        'class="w-full px-4 py-3 rounded-xl border border-[var(--color-gaba-border)] focus:ring-2 focus:ring-[var(--color-gaba-blue)] focus:border-transparent outline-none transition-all bg-[var(--color-gaba-surface-alt)] focus:bg-[var(--color-gaba-surface)] resize-none text-[var(--color-gaba-navy)]"',
        'class="w-full px-3 py-2.5 sm:px-4 sm:py-3 text-sm sm:text-base rounded-lg sm:rounded-xl border border-[var(--color-gaba-border)] focus:ring-2 focus:ring-[var(--color-gaba-blue)] focus:border-transparent outline-none transition-all bg-[var(--color-gaba-surface-alt)] focus:bg-[var(--color-gaba-surface)] resize-none text-[var(--color-gaba-navy)]"'
    )
    # 1.6 select
    content = content.replace(
        'class="w-full px-4 py-3 rounded-xl border border-[var(--color-gaba-border)] focus:ring-2 focus:ring-[var(--color-gaba-blue)] focus:border-transparent outline-none transition-all bg-[var(--color-gaba-surface-alt)] focus:bg-[var(--color-gaba-surface)] appearance-none text-[var(--color-gaba-navy)]"',
        'class="w-full px-3 py-2.5 sm:px-4 sm:py-3 text-sm sm:text-base rounded-lg sm:rounded-xl border border-[var(--color-gaba-border)] focus:ring-2 focus:ring-[var(--color-gaba-blue)] focus:border-transparent outline-none transition-all bg-[var(--color-gaba-surface-alt)] focus:bg-[var(--color-gaba-surface)] appearance-none text-[var(--color-gaba-navy)]"'
    )

    # 2. Labels
    content = content.replace(
        'class="block text-sm font-semibold text-[var(--color-gaba-navy)] mb-2"',
        'class="block text-xs sm:text-sm font-semibold text-[var(--color-gaba-navy)] mb-1.5 sm:mb-2"'
    )
    content = content.replace(
        'class="block text-sm font-semibold text-[var(--color-gaba-navy)] mb-3"',
        'class="block text-xs sm:text-sm font-semibold text-[var(--color-gaba-navy)] mb-2 sm:mb-3"'
    )
    content = content.replace(
        'class="block text-sm font-semibold text-[var(--color-gaba-navy)] mb-2 flex items-center gap-2"',
        'class="block text-xs sm:text-sm font-semibold text-[var(--color-gaba-navy)] mb-1.5 sm:mb-2 flex items-center gap-2"'
    )

    # 3. Section Titles
    content = content.replace(
        'class="text-xl font-bold text-[var(--color-gaba-blue)]"',
        'class="text-base sm:text-xl font-bold text-[var(--color-gaba-blue)] tracking-tight"'
    )

    # 4. Grids & Gaps (Form specific)
    # Specifically spaces in the form
    content = content.replace('class="grid grid-cols-1 md:grid-cols-2 gap-6"', 'class="grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-6"')
    content = content.replace('class="grid grid-cols-1 md:grid-cols-3 gap-6"', 'class="grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-6"')
    
    # 5. Section gaps
    content = content.replace('class="space-y-6"', 'class="space-y-4 sm:space-y-6"')
    content = content.replace('class="border-b border-[var(--color-gaba-border)] pb-2 mb-4"', 'class="border-b border-[var(--color-gaba-border)] pb-1.5 sm:pb-2 mb-3 sm:mb-4"')

    # 6. Radios & Checkboxes
    content = content.replace(
        'class="w-4 h-4 text-[var(--color-gaba-blue)] focus:ring-[var(--color-gaba-blue)] accent-[var(--color-gaba-blue)]"',
        'class="w-3.5 h-3.5 sm:w-4 sm:h-4 text-[var(--color-gaba-blue)] focus:ring-[var(--color-gaba-blue)] accent-[var(--color-gaba-blue)]"'
    )
    content = content.replace(
        'class="w-4 h-4 text-[var(--color-gaba-blue)] rounded accent-[var(--color-gaba-blue)]"',
        'class="w-3.5 h-3.5 sm:w-4 sm:h-4 text-[var(--color-gaba-blue)] rounded accent-[var(--color-gaba-blue)]"'
    )
    content = content.replace(
        'class="text-sm text-[var(--color-gaba-navy)]"',
        'class="text-xs sm:text-sm text-[var(--color-gaba-navy)]"'
    )

    # 7. Privacy Box
    content = content.replace(
        'class="bg-[var(--color-gaba-surface-alt)] p-4 rounded-xl border border-[var(--color-gaba-border)] flex items-start gap-4 hover:border-[var(--color-gaba-blue)]/50 transition-colors"',
        'class="bg-[var(--color-gaba-surface-alt)] p-3 sm:p-4 rounded-lg sm:rounded-xl border border-[var(--color-gaba-border)] flex items-start gap-3 sm:gap-4 hover:border-[var(--color-gaba-blue)]/50 transition-colors"'
    )
    content = content.replace(
        'class="w-5 h-5 text-[var(--color-gaba-blue)] focus:ring-[var(--color-gaba-blue)] rounded accent-[var(--color-gaba-blue)]"',
        'class="w-4 h-4 sm:w-5 sm:h-5 text-[var(--color-gaba-blue)] focus:ring-[var(--color-gaba-blue)] rounded accent-[var(--color-gaba-blue)] mt-0.5"'
    )
    content = content.replace(
        'class="text-sm text-[var(--color-gaba-navy)] cursor-pointer leading-relaxed"',
        'class="text-[11px] sm:text-sm text-[var(--color-gaba-navy)] cursor-pointer leading-relaxed"'
    )

    # 8. Submit Button
    content = content.replace(
        'class="w-full py-4 rounded-xl bg-[var(--color-gaba-green)] text-white text-lg font-bold hover:bg-opacity-90 transition-all shadow-md hover:shadow-xl transform hover:-translate-y-1 flex justify-center items-center gap-2 group"',
        'class="w-full py-3.5 sm:py-4 rounded-lg sm:rounded-xl bg-[var(--color-gaba-green)] text-white text-base sm:text-lg font-bold hover:bg-opacity-90 transition-all shadow-md hover:shadow-xl transform hover:-translate-y-0.5 flex justify-center items-center gap-2 group"'
    )
    content = content.replace(
        'class="text-xs text-center text-[var(--color-gaba-navy)]/60 mt-4 flex items-center justify-center gap-1.5 flex-wrap"',
        'class="text-[10px] sm:text-xs text-center text-[var(--color-gaba-navy)]/60 mt-3 sm:mt-4 flex items-center justify-center gap-1.5 flex-wrap opacity-80"'
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("Form replaced successfully!")

if __name__ == "__main__":
    main()
