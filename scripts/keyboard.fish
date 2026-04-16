#!/usr/bin/env fish

# Define layouts in desired order
set layouts us no

# Get current layout(s)
set current_raw (setxkbmap -query | string match -r 'layout:\s+(.+)' | string replace -r 'layout:\s+' '')

# Split on comma → take first active layout
set current (string split ',' $current_raw)[1]

# Fallback if empty
if test -z "$current"
    set current $layouts[1]
end

# Find index (1-based)
set index 1
for i in (seq (count $layouts))
    if test "$layouts[$i]" = "$current"
        set index $i
        break
    end
end

# Compute next index safely
set count (count $layouts)
set next_index (math "($index % $count) + 1")

# Get next layout
set next_layout $layouts[$next_index]

# Apply it
setxkbmap $next_layout

echo "Switched to layout: $next_layout"