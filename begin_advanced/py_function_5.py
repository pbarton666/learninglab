#py_function_5.py

def outer_space(outer_input):
	"outer-most function"
	last_answer=outer_input

	def inner_space(inner_input):
		"inner-most function"
		nonlocal last_answer
		last_answer += inner_input
		return last_answer
	return inner_space
		
MEANING_OF_LIFE=42
original = outer_space(MEANING_OF_LIFE)
print("The original meaning of life is {}".format(original(0)))

tweak=3
new_meaning = original(tweak)
print("But now we think it's a bit more: {}".format(new_meaning))

next_new_meaning = original(tweak)
print("... and now: {}".format(next_new_meaning))


