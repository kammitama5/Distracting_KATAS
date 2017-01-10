def sort_gift_code code
  code.unpack("c*").sort.pack("c*")
end

