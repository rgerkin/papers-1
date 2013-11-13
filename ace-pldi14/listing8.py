import examples.clx as clx, numpy, listing1, listing5

clx.default_ctx = clx.Context.for_device(0, 0)

input = numpy.ones((1024,))
d_input = clx.to_device(input)
d_output = clx.alloc(like=input)

listing1.map(d_input, d_output, listing5.add_5, 
  global_size=d_in.shape, local_size=(128,))

assert (cl.from_device(d_out) == input + 5).all()