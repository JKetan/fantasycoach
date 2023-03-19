p=pd.read_csv('CompleteDataset.csv')
		set = pd.DataFrame(p)
		p_name = self.Entry1.get()
		t_content = []
		for row in set:
			if p_name == row['Name']:
				self.text = Text(top)
				self.text.place(relx=0.35, rely=0.522,height=63, relwidth=0.277)
				self.text.configure(font="TkFixedFont", width = 500, height = 200)
				self.text.insert(INSERT,''' Name: ''' + row['Name'] + '''\n''' +
							''' Age: ''' + row['Age'] + '''\n''' +
							''' Club: ''' + row['Club'] + '''\n''' +
							''' Overall: ''' + row['Overall'] + '''\n''' +
							''' Potential: ''' + row['Potential'] + '''\n''' +
							''' Value: ''' + row['Value'] + '''\n'''
						)

