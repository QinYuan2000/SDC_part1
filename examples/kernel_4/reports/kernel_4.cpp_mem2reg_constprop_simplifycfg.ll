; ModuleID = 'kernel_4.cpp_mem2reg_constprop.ll'
source_filename = "src/kernel_4.cpp"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

; Function Attrs: noinline nounwind uwtable
define i32 @_Z8kernel_4iiii(i32 %a, i32 %b, i32 %c, i32 %n) #0 {
entry:
  %add = add nsw i32 %b, 50
  %add1 = add nsw i32 100, %n
  %mul = mul nsw i32 %add, %add1
  %add2 = add nsw i32 40, %c
  %mul3 = mul nsw i32 %mul, %add2
  %add4 = add nsw i32 10, %a
  %mul5 = mul nsw i32 %mul3, %add4
  %mul6 = mul nsw i32 %n, 10000
  %cmp = icmp sgt i32 %mul5, %mul6
  br i1 %cmp, label %if.then, label %if.else

if.then:                                          ; preds = %entry
  %add7 = add nsw i32 %n, %c
  %div = sdiv i32 %mul5, %add7
  br label %if.end

if.else:                                          ; preds = %entry
  %add8 = add nsw i32 %mul5, %c
  %rem = srem i32 %b, %add8
  br label %if.end

if.end:                                           ; preds = %if.else, %if.then
  %a.addr.0 = phi i32 [ %div, %if.then ], [ %rem, %if.else ]
  %mul9 = mul nsw i32 %a.addr.0, %n
  %add10 = add nsw i32 %c, %b
  %mul11 = mul nsw i32 %add10, %b
  %xor = xor i32 %mul9, %mul11
  ret i32 %xor
}

; Function Attrs: noinline norecurse nounwind uwtable
define i32 @main() #1 {
entry:
  %call = call i32 @rand() #3
  %rem = srem i32 %call, 10
  %call1 = call i32 @rand() #3
  %rem2 = srem i32 %call1, 10
  %call3 = call i32 @rand() #3
  %rem4 = srem i32 %call3, 10
  %call5 = call i32 @rand() #3
  %rem6 = srem i32 %call5, 10
  %call7 = call i32 @_Z8kernel_4iiii(i32 %rem, i32 %rem2, i32 %rem4, i32 %rem6)
  ret i32 0
}

; Function Attrs: nounwind
declare i32 @rand() #2

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { noinline norecurse nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nounwind "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { nounwind }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 6.0.1 (http://github.com/llvm-mirror/clang 2f27999df400d17b33cdd412fdd606a88208dfcc) (http://github.com/llvm-mirror/llvm 5136df4d089a086b70d452160ad5451861269498)"}