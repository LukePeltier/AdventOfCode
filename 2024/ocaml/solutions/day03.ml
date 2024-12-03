let find_matches line pattern =
  let matches = Re.all pattern line in
  List.map
    (fun m ->
      (int_of_string (Re.Group.get m 1), int_of_string (Re.Group.get m 2)))
    matches

let solve () =
  let pattern = Re.Perl.compile_pat "mul\\((\\d{1,3}),(\\d{1,3})\\)" in
  let ic = open_in "inputs/day03.test" in
  let rec process_file acc =
    try
      let line = input_line ic in
      let matches = find_matches line pattern in
      process_file (matches @ acc)
    with End_of_file ->
      close_in ic;
      acc
  in
  let result = process_file [] in
  Printf.printf "Pairs: %s\n" (Utils.string_of_tuple_list result);
  let sum =
    List.fold_left
      (fun acc x ->
        let x, y = x in
        acc + (x * y))
      0 result
  in

  Printf.printf "Sum: %d\n" sum

let solve_bonus () = print_endline "Not yet implemented"
