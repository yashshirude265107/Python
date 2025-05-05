# Sample data
website_visitors = {"Alice", "Bob", "carcol", "dave"}
email_clickers = {"bob", "dave", "eve", "frank"}

#Union : All Users who showed interest in any way
all_interested = website_visitors.union(email_clickers)
print("Union of both the set", all_interested)

#Intersection : users who both visited and clicked
engaged_users = website_visitors.intersection(email_clickers)
print("Intersection of both the set", engaged_users)

#Differnce : users who visited the site but didnot click the email
site_only_users = website_visitors.difference(email_clickers)
print("Difference of both the set", site_only_users)

#Symmetric difference : users who engaged in only one of the action
partial_engaged = website_visitors.symmetric_difference(email_clickers)
print("Symmetric difference of both the set", partial_engaged)