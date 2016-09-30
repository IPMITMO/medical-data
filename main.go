package main

import (
    "fmt"
    "github.com/extrame/xls"
)

func read(name string) {
if xlFile, err := xls.Open(name, "utf-8"); err == nil {
		if sheet1 := xlFile.GetSheet(0); sheet1 != nil {
			fmt.Print("Total Lines ", sheet1.MaxRow, sheet1.Name)
			col1 := sheet1.Rows[0].Cols[0]
			col2 := sheet1.Rows[0].Cols[0]
            col3 := sheet1.Rows[0].Cols[0]
			for i := 0; i <= (int(sheet1.MaxRow)); i++ {
				row1 := sheet1.Rows[uint16(i)]
				col1 = row1.Cols[0]
				col2 = row1.Cols[1]
				col3 = row1.Cols[2]
                fmt.Println(col1)
				fmt.Print("\n", col1.String(xlFile), ",", col2.String(xlFile) , ",",col3.String(xlFile))
			}
		}
	}

}

func main(){
//    read("area.xls")
    read("street.xls")
}
