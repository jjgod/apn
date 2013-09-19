// AssignPhoneticName.m

#import <AddressBook/AddressBook.h>
#import <CoreFoundation/CoreFoundation.h>

@interface NSString (PhoneticAdditions)
- (NSString*)phoneticString;
@end

@implementation NSString (PhoneticAdditions)

- (NSString*)phoneticString {
  NSMutableString* string = [self mutableCopy];
  CFStringTransform((CFMutableStringRef)string,
                    NULL,
                    kCFStringTransformMandarinLatin,
                    NO);
  NSString* result = nil;
  if (![string isEqualToString:self]) {
    result = [[string stringByReplacingOccurrencesOfString:@" " withString:@""]
        capitalizedString];
  }
  [string release];
  return result;
}

@end

const char* emptyIfNil(NSString* string) {
  return string ? [string UTF8String] : "";
}

int main(int argc, char* argv[]) {
  @autoreleasepool {
    ABAddressBook* ab = [ABAddressBook sharedAddressBook];
    for (ABPerson* person in [ab people]) {
      NSString* lastName = [person valueForProperty:kABLastNameProperty];
      NSString* phoneticLastName = [lastName phoneticString];
      NSString* firstName = [person valueForProperty:kABFirstNameProperty];
      NSString* phoneticFirstName = [firstName phoneticString];
      if (phoneticLastName)
        [person setValue:phoneticLastName forProperty:kABLastNamePhoneticProperty];
      if (phoneticFirstName)
        [person setValue:phoneticFirstName forProperty:kABFirstNamePhoneticProperty];
      if (phoneticLastName || phoneticFirstName)
        printf("Update %s%s (%s %s)\n",
               emptyIfNil(lastName), emptyIfNil(firstName),
               emptyIfNil(phoneticLastName), emptyIfNil(phoneticFirstName));
    }
    [ab save];
  }
  return 0;
}
