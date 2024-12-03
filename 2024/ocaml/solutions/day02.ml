let solve () =
  let ic = open_in "inputs/day02.input" in
  let rec process_lines list1 list2 =
    try
      let line = input_line ic in
      let words =
        line |> String.split_on_char ' ' |> List.filter (fun s -> s <> "")
      in
      match words with
      | first :: second :: _ ->
          let n1 = int_of_string first in
          let n2 = int_of_string second in
          process_lines (n1 :: list1) (n2 :: list2)
      | _ -> process_lines list1 list2
    with
    | End_of_file ->
        close_in ic;
        (list1, list2)
    | Failure _ -> process_lines list1 list2
  in

  let list1, list2 = process_lines [] [] in
  let sorted1 = List.sort compare list1 in
  let sorted2 = List.sort compare list2 in

  let sum =
    List.fold_left2 (fun acc x y -> acc + abs (x - y)) 0 sorted1 sorted2
  in
  Printf.printf "Sum of differences: %d\n" sum

let solve_bonus () = print_endline "Not yet implemented"
